import math

def area_circle(r):
    """ Calculates area of circle
    Parameters
        r: radius
    Returns
        area of circle
    """
    return math.pow(r,2)*math.pi

def is_prime_number(n):
    """ Checks if given number is a prime
    Parameters
        n: number
    Returns
        True or False
    """
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count+=1
    if count == 2:
        return True
    return False

