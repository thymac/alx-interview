def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve 'n' characters 'H'.

    :param n: The desired number of characters 'H'
    :type n: int
    :return: The minimum number of operations needed to achieve 'n' characters 'H'
    :rtype: int
    """
    # Handle the case when n is not achievable
    if n <= 1:
        return 0

    factors = []  # List to store prime factors of n
    divisor = 2  # Start with the smallest prime divisor
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)  # Add current divisor to the list of factors
            n //= divisor  # Divide n by the current divisor
        else:
            divisor += 1  # Increment divisor to check the next number

    if len(factors) == 0:
        return 0  # If no prime factors found, n is not achievable

    return sum(factors)  # Return the sum of prime factors as the minimum operations

