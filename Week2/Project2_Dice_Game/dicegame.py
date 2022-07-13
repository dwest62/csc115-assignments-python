from dealer import DiceDealer
from funds import Funds
from dice.dice import Dice

class DiceGame:
    def __init__(self):
        self.dice = Dice()
        self.funds = Funds(350)
        self.dealer = DiceDealer(self.funds, self.dice)
        self.dealer.welcome()
    
    def play(self):
        self.play_round()
        response = self.dealer.check_if_player_cont()
        while response in ("Y, y"):
            self.play_round()
            if self.funds.curr_money == 0:
                print("Sorry, you are out of money.")
                exit("See you later!")
        exit(f"Your final score is $ {self.funds.curr_money:,.2f}")

    def play_round(self):
        bet = self.dealer.get_player_bet()
        guess = self.dealer.get_player_guess()
        self.dealer.roll_dice()
        self.process_round_result(guess, bet)
    
    def process_round_result(self, guess, bet):
        d1, d2 = self.dice.curr_vals
        if guess == d1 + d2:
            wl = "won"
            if d1 == d2:
                print("Big Winner!")
                bet = bet * 2
            self.funds.add(bet)
        else:
            wl = "lost"
            self.funds.sub(bet)
        print(f"You {wl} $ {bet:,.2f}.")
        print(f"Your current balance is $ {self.funds.curr_money:,.2f}.")