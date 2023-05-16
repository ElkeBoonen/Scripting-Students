def calculate(name1,name2):
    """ Calculate the love percentage
    Parameters
        name1: string
        name2: string
    Return
        the percentage
    """
    len_name1 = len(name1)
    len_name2 = len(name2)
    result = abs(len_name1-len_name2)

    if (result <= 2):
        return "90% match"
    elif (result <= 4):
        return "80% match"
    elif (result <= 6):
        return "70% match"
    elif (result <= 8):
        return "60% match"
    else:
        return "no match!"
    
from difflib import SequenceMatcher 

def calculate2(name1,name2):
    """ Calculate the love percentage with similarity check
    Parameters
        name1: string
        name2: string
    Return
        the percentage
    """
    result = round(SequenceMatcher(None, name1, name2).ratio() * 100,0)
    return str(result) + "% match"
    