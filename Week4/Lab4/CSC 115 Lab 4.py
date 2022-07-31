import random

def main():
    #--------------------------
    # Randomly pick a scrambled word from the list.
    # Asks the user to guess it.
    # Ask again if the guess is wrong.  Repeat until the guess is right.
    # If guess is right, ask if user wants another game.
    #--------------------------
    display_banner()
    (scrambled_list, answer_list) = load_words('Week4\Lab4\CSC 115 Lab 4_Words.txt')
    app = ScrambledApp(scrambled_list, answer_list)
    app.run()


class ScrambledApp:
    def __init__(self, scrambled_list: list, answer_list: list) -> None:
        self.scrambled_list = scrambled_list
        self.answer_list = answer_list
        self.guesses = 0

    def run(self):
        if len(self.scrambled_list) == 0:
            print("You have guessed all the words. Great job!")
        else:
            self.pick_word()
            self.loop_round()

    def loop_round(self):
        print(f"Scrambled word is: {self.pick}")
        user_answer = self.prompt_answer()

        if user_answer == self.answer:
            self.handle_correct_answer()
        else:
            self.handle_wrong_answer()
    
    def handle_correct_answer(self):
        self.answer_list.remove(self.answer)
        self.scrambled_list.remove(self.pick)
        print("You got it!")
        self.guesses = 0
        if self._prompt_continue("Another game? (Y/N): "):
            self.run()
        else:
            print("bye")
    
    def handle_wrong_answer(self):
        print("Wrong answer. Try again!")
        if self.guesses < len(self.answer) - 1:
            self.guesses += 1
        self.give_hint()
        self.loop_round()
    
    def _prompt_continue(self, prompt) -> bool:
        maybe_continue = input(prompt)
        while maybe_continue not in ["Y", "y", "N", "n"]:
            print(f"Invalid input {maybe_continue}, enter Y or N.")
            maybe_continue = input(prompt)
        return maybe_continue in ["Y", "y"]
    
    def pick_word(self):
        rand = random.randint(0, len(self.scrambled_list) - 1)
        self.pick, self.answer = self.scrambled_list[rand], self.answer_list[rand]
    
    def prompt_answer(self):
        user_answer = input("What is the word? ")
        return user_answer
        
    def give_hint(self):
        print(f"Hint #{self.guesses}: {self.answer[:self.guesses]}")

def display_banner():
    print("""
 __                               _      _            _ 
/ _\  ___  _ __  __ _  _ __ ___  | |__  | |  ___   __| |
\ \  / __|| '__|/ _` || '_ ` _ \ | '_ \ | | / _ \ / _` |
_\ \| (__ | |  | (_| || | | | | || |_) || ||  __/| (_| |
\__/ \___||_|   \__,_||_| |_| |_||_.__/ |_| \___| \__,_|
                                                        
""")

def load_words(filename):
    #load file containing scrambled word and answer.
    #scrambled word and answer are separated by :

    scrambled_list = []
    answer_list = []
    with open(filename, 'r') as f:
        for line in f:
            (s,a) = line.strip().split(":")
            scrambled_list+=[s]
            answer_list+=[a]
    return (scrambled_list, answer_list) 


if __name__ == "__main__":
    main()
