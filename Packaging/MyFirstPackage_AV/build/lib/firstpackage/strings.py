def Reverse(text):
    """Reverse a string
    Parameters:
        string text
    Returns
        reversed text
    """
    return text[::-1]

def Ascii(text):
    """Converts string to separate ASCII-values
    Parameters:
        string text
    Returns 
        string of ASCII values
    """
    result=""
    for l in text:
        result += str(ord(l)) + " "
    return result
