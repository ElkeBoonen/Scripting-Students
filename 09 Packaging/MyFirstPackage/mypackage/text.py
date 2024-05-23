def OddEvenLength(text):
    """ Returns odd or even length of given text
        Parameters:
            text (string): given text
        Returns:
            odd or even length
    """
    length = len(text)
    if length % 2 == 0:
        return "even length"
    else:
        return "odd length"
  
def AInText(text):
    """ Checks if there is an A in the text
        Parameters:
            text (string): given text
        Returns:
            True or False
    """
    for char in text:
        if char == "A" or char == "a":
            return True
    return False
