# This program engages user in cli-based dice game. The user offers a guess as to the sum
# of the dice which are rolled. If the sum of the dice matches the users guess, they win.
# If the dice match each other, the winning amount = 2xs the bet, else, the winning amount
# is equal to the bet placed.
# If the dice do not match each other, the player loses and forfeits the amount they bet.
# The game ends when the player runs out of money or chooses to end the round.

from dicegame import DiceGame

def main():
    game = DiceGame()
    game.play()

if __name__ == "__main__":
    main()