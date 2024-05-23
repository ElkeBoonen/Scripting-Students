def OddEvenLength(text):
    length = len(text)
    if length % 2 == 0:
        return "even length"
    else:
        return "odd length"
    
def AInText(text):
    for char in text:
        if char == "A" or char == "a":
            return True
    return False
