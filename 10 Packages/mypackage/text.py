import re

def novowels(word):
    """ Returns a word without vowels
    Parameters:
        a string
    Returns:
        a string
    """
    chars = re.split('[aeuio]',word)
    return "".join(chars)

def reverse(word):
    """ Returns a reversed word
    Parameters:
        a string
    Returns:
        a string
    """
    return word[::-1]

