def Average(list):
    sum = 0
    count = 0.0
    for nr in list:
        sum += nr
        count += 1
    return sum / count
    
def Max(list):
    max = list[0]
    for nr in list:
        if nr > max:
            max = nr
    return max

def Min(list):
    min = list[0]
    for nr in list:
        if nr < min:
            min = nr
    return min