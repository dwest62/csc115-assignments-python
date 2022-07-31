class Calc:
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

    @staticmethod
    def min(*floats: float, is_sorted: bool = False) -> float:
        if not is_sorted:
            floats = sorted(list(floats))
        return floats[0]

    @staticmethod
    def max(*floats: float, is_sorted: bool = False) -> float:
        if not is_sorted:
            floats = sorted(list(floats))
        return floats[-1]

    def mean(self, *floats: float):
        total = self.add(*floats)
        return total/len(floats)

    @staticmethod
    def median(*floats: float, is_sorted: bool = False):
        if not is_sorted:
            floats = sorted(floats)
        return floats[len(floats)//2]

class GradeStatsCalc(Calc):
    _stats = {}
    def __init__(self) -> None:
        pass
   
    def set_stats(self, raw_data: list):
        arr = [int(stat) for stat in raw_data]

        stats = {
            "Min": int(self.min(*arr)),
            "Max": int(self.max(*arr)),
            "Mean": int(self.mean(*arr)),
            "Median": int(self.median(*arr))
        }
        self._stats = stats

    def get_stats_str(self) -> str:
        s = ""
        for k, v in self._stats.items():
            s += f"{k:12} = {v}\n"
        return s   
    
    def display_stats(self) -> None:
        print("Below are the computed values.")
        print(self.get_stats_str())