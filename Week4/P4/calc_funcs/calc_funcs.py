
def add(*floats) -> float:
    total = 0
    for n in floats:
        total += n
    return total

def sub(minuend: float, *subtrahends: float) -> float:
    difference = minuend
    for subtrahend in subtrahends:
        difference -= subtrahend
    return difference   
    
def mul(*floats: float) -> float:
    product = floats[0]
    for n in floats[1:]:
        product *= n
    return product
   
def div(dividend: float, *divisors: float) -> float:
    quotient = dividend
    for n in divisors:
        quotient /= n
    return quotient
  
def abs(*floats: float) -> float:
    # This is already a built in function: abs().
    # For the purpose of this assignment this will not be used.
    f = [str(abs(f)) for f in floats]
    return ' '.join(f)

def min(*floats: float, is_sorted: bool = False) -> float:
    if not is_sorted:
        floats = sorted(list(floats))
    return floats[0]

def max(*floats: float, is_sorted: bool = False) -> float:
    if not is_sorted:
        floats = sorted(list(floats))
    return floats[-1]

def mean(*floats: float):
    total = add(*floats)
    return total/len(floats)

def median(*floats: float, is_sorted: bool):
    if not is_sorted:
        floats = sorted(floats)
    return floats[len(floats)//2]
