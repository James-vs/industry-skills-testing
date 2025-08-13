def factorial(n):
    """
    Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    
    if n < 0:
        raise ValueError("Only use non-negative integers.")

    if isinstance(n, str):
        raise TypeError("Strings are not accepted. Only use integers.")

    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial
