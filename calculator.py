def to_binary(n: int) -> str:
    """Cconvert"""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("error")
    if n < 0 or n > 100:
        raise ValueError("error")
    return bin(n)[2:]
