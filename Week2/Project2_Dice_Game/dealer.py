from random import randint
from funds import Funds
from dice.dice import Dice

class DiceDealer():
    def __init__(self, player_fund: Funds, dice: Dice):
        self.anger_level = 0
        self.err_msgs = [
            "Cheeky answer, but that will get us nowhere.",
            "That answer doesn't work buckaroo.",
            "I'm growing impatient.",
            "Last chance.",
            "\nWe are done here. Gerald, please escort our guest out."
        ]
        self.player_fund = player_fund
        self.dice = dice

    def welcome(self):
        print("\nWelcome to Dice Game.\n")
        self.dice.roll()
        print()
        print(f"You are given $ {self.player_fund.curr_money:,.2f} to start.")
        print("Two dice will be rolled. To win you must guess the sum.")
        print("You can't play once you run out of money.\n")

    def roll_dice(self):
        print("\nRolling dice...")
        self.dice.roll()

    def get_player_bet(self):
        funds = self.player_fund.curr_money
        try:
            bet = float(input("How much are you betting? "))
        except:
            self.handle_bad_input("bet")
            bet = self.get_player_bet()
        while bet < 0 or bet > funds:
            self.handle_bad_input("bet")
            bet = self.get_player_bet()
        self.calm_dealer()
        return bet

    def get_player_guess(self):
        try:
            guess = int(input("What is the sum of the two dice? "))
            if guess > 12 or guess < 2:
                print("You do realize that this guess is... nvm it's your money.")
        except:
            self.handle_bad_input("guess")
            guess = self.get_player_guess()
        self.calm_dealer()
        return guess
    
    def check_if_player_cont(self):
        prompt = "Do you want another game? Y/N "
        player_response = input(prompt)
        while player_response not in ("Y","y","N","n"):
            self.anger_dealer()
            player_response = input(prompt)
        self.calm_dealer()
        print("")
        return player_response
    
    def handle_bad_input (self, type = "err"):
        self.anger_dealer()
        randbet = f"{self.player_fund.curr_money / randint(1,4):,.0f}"
        if type == "bet":
            print(f"Try again. You could try betting {randbet}.\n")
        else:
            print("Try again.\n")
    
    def calm_dealer(self):
        if self.anger_level > 0:
            self.anger_level -= 1

    def anger_dealer(self):
        print(self.err_msgs[self.anger_level], end=" ")
        self.anger_level += 1
        if self.anger_level == len(self.err_msgs):
            self.kick_out_player()

    def kick_out_player(self):
        exit(
            "\nYou have been kicked out of Dice Game!\n" +
            f"Your final score is ${self.player_fund.curr_money:,.2f}."
        )