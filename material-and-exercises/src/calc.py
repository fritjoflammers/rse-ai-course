def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Calculate the difference between a and b.

    Args:
        a (float): The minuend.
        b (float): The subtrahend.

    Returns:
        float: The result of a - b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
