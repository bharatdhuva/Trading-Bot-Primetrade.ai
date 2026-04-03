def validate_symbol(symbol: str) -> bool:
    if not symbol or not symbol.isalnum():
        return False
    return True

def validate_positive_float(val: str) -> bool:
    try:
        f = float(val)
        if f > 0:
            return True
        return False
    except ValueError:
        return False
