def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
