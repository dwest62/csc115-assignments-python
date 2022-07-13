class Funds():
    def __init__(self, starting_amount: float):
        self.curr_money = starting_amount

    def add(self, amount):
        self.curr_money += amount

    def sub(self, amount):
        self.curr_money -= amount    
