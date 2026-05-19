def sumofmulti(number):
    """ Returns the sum of the multiplication table
    Parameters:
        a number
    Returns:
        a number
    """
    sum = 0
    for i in range(1,10):
        sum += i*number
    return sum


