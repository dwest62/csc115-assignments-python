from typing import List
from types import FunctionType
from mat.cal_funcs import CalcFuncs

class CalcApp(CalcFuncs):
    def __init__(self) -> None:
        super().__init__()
    
    def run_app(self):
        user_input = input()
        if user_input == "quit": return
        try:
            print(self.new_calculation(user_input))
        except:
            print("Error parsing input. Try again or type quit to exit.")
        finally:
            self.run_app()

    def new_calculation(self, user_input: str) -> float:
        self.set_user_input(user_input)
        nums = self.parse_nums()
        curr_function = self.parse_f()
        return curr_function(*nums)
    
    def set_user_input(self, user_input: str) -> None:
        self.user_input = user_input

    def parse_nums(self) -> List[float]:
        nums = []
        for n in self.user_input.split(" ")[1:]:
            nums.append(float(n))
        return nums
    
    def parse_f(self) -> FunctionType:
        key = self.user_input.split(" ")[0]
        f = self.calc_func_map.get(key)
        return f