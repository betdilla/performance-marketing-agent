def f(row, key):
    value = row.get(key, "")
    if value in ("", None):
        raise ValueError("Missing required metric: " + key)
    return float(value)

def pct_change(current, previous):
    if previous == 0:
        raise ValueError("Cannot calculate percentage change from zero")
    return (current - previous) / previous

def ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return numerator / denominator
