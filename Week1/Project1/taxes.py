# This program calculates the user's net pay based on their tax bracket.
# It accepts std inputs for first name, last name, monthly gross pay, and number of dependants.
# After calculation, program prints user info: name, gross pay,["money"] dependents, tax rate, and net pay.

def main():
    user = Taxpayer()
    user.print_tax_info()

class Taxpayer(object):
    def __init__(self):
        self.first_name = input("\nEnter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.name = f"{self.first_name} {self.last_name}"
        self.gross_pay = float(input("Enter your gross pay: "))
        self.dependents = int(input("Enter number of dependents: "))
        self.tax = self.get_bracketed_tax_rate()
        self.net_pay = self.gross_pay - self.gross_pay * self.tax

    # Returns tax rate based on dependents bracket
    def get_bracketed_tax_rate(self):
        if 0 <= self.dependents <= 1:
            return .25              # 0 - 1 | .25
        if self.dependents <= 3:
            return .20              # 2 - 3 | .20
        else:
            return .15              # 4 +   | .15

    def print_tax_info(self):
        f_money = lambda money: "$" + "{:,.2f}".format(money) # formats to $
        f_tax = lambda tax: "{:.0f}".format(tax * 100) + "%" # formats to %
        f_desc = lambda desc: "{:12}".format(desc) # formats width to align output
        print (
            "",
            f"{f_desc('Name:')}{self.name}",
            f"{f_desc('Gross pay:')}{f_money(self.gross_pay)}",
            f"{f_desc('Dependents:')}{self.dependents}",
            f"{f_desc('Tax rate:')}{f_tax(self.tax)}",
            f"{f_desc('Net Pay:')}{f_money(self.net_pay)}",
            "",
            sep="\n"
        )

if __name__ == "__main__":
    main()