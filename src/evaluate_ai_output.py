import json
import re
from pathlib import Path


VALID_DECISIONS = {"SCALE", "HOLD", "TEST", "FIX", "STOP"}
REQUIRED_FIELDS = [
    "OBSERVATION", "DIAGNOSIS", "EVIDENCE", "CONFIDENCE", "DECISION",
    "ACTION", "EXPECTED IMPACT", "RISK", "VALIDATION",
]


def parse_case_sections(text):
    matches = list(re.finditer(r"(?im)^##\s*Case\s+([A-Z0-9_-]+)\s*$", text))
    sections = {}
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[match.group(1)] = text[start:end]
    return sections


def field_value(section, field):
    pattern = rf"(?ims)^\s*{re.escape(field)}\s*:\s*(.*?)(?=^\s*(?:{'|'.join(map(re.escape, REQUIRED_FIELDS))})\s*:|\Z)"
    match = re.search(pattern, section)
    return match.group(1).strip() if match else None


def evaluate(text, expected):
    sections = parse_case_sections(text)
    failures = []
    results = {}

    for case_id, rule in expected.items():
        section = sections.get(case_id)
        case_failures = []
        if section is None:
            failures.append(f"{case_id}: missing case section")
            results[case_id] = {"passed": False, "failures": ["missing case section"]}
            continue

        fields = {name: field_value(section, name) for name in REQUIRED_FIELDS}
        missing = [name for name, value in fields.items() if not value]
        if missing:
            case_failures.append("missing fields: " + ", ".join(missing))

        decision_text = fields.get("DECISION") or ""
        decision_match = re.search(r"\b(SCALE|HOLD|TEST|FIX|STOP)\b", decision_text.upper())
        decision = decision_match.group(1) if decision_match else None
        if decision not in VALID_DECISIONS:
            case_failures.append("invalid or missing primary decision")
        if decision in rule.get("forbidden", []):
            case_failures.append(f"forbidden decision: {decision}")

        searchable = " ".join(v or "" for v in fields.values()).lower()
        for phrase in rule.get("must_surface", []):
            tokens = [t for t in re.findall(r"[a-z]+", phrase.lower()) if len(t) > 3]
            if tokens and not all(token in searchable for token in tokens):
                case_failures.append(f"required concept not surfaced: {phrase}")

        confidence = (fields.get("CONFIDENCE") or "").upper()
        if not re.search(r"\b(LOW|MEDIUM|HIGH)\b", confidence):
            case_failures.append("confidence must be LOW, MEDIUM or HIGH")

        results[case_id] = {
            "passed": not case_failures,
            "decision": decision,
            "failures": case_failures,
        }
        failures.extend(f"{case_id}: {x}" for x in case_failures)

    return {"passed": not failures, "failures": failures, "cases": results}


def load_expected(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))
