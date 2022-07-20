class CalcFuncs:
    func_map = {}

    def __init__(self) -> None:
        for f in (self.add, self.sub, self.mul, self.div, self.abs):
            self.func_map[f.__name__] = f
            self.func_map[f.__name__].count = 0
            
    @staticmethod
    def add(*floats) -> float:
        total = 0
        for n in floats:
            total += n
        return total

    @staticmethod
    def sub(minuend: float, *subtrahends: float) -> float:
        difference = minuend
        for subtrahend in subtrahends:
            difference -= subtrahend
        return difference   
        
    @staticmethod
    def mul(*floats: float) -> float:
        product = floats[0]
        for n in floats[1:]:
            product *= n
        return product
    
    @staticmethod   
    def div(dividend: float, *divisors: float) -> float:
        quotient = dividend
        for n in divisors:
            quotient /= n
        return quotient
    
    @staticmethod  
    def abs(*floats: float) -> float:
        # This is already a built in function: abs().
        # For the purpose of this assignment this will not be used.
        f = [str(abs(f)) for f in floats]
        return ' '.join(f)