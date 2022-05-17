def Sum(x,y):
    """Calculate sum
    Parameters: 
        number x
        number y
    Returns
        sum of x and y
    """
    return x+y

def Factorial(x):
    """Calculate Factorial
    Parameters:
        int x
    Returns
        factorial of x
    """
    result = 1
    for i in range(2,x+1):
        result = result * i
    return result

def Odd(x):
    """Determine if number is odd
    Parameters:
        number x
    Returns
        true or false
    """
    if (x % 2 == 0):
        return False
    return True