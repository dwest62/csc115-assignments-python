def main():
    user_tax_info = UserTaxInfo()
    user_tax_info.print_user_tax_info()

class User(object):
    def __init__(self):
        self.first_name = input("\nEnter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.name = f"{self.first_name} {self.last_name}"

class UserTaxInfo(User):
	def __init__(self):
		super().__init__()
		self.gross_pay = float(input("Enter your gross pay: "))
		self.dependents = int(input("Enter number of dependents: "))
		self.tax = self.get_tax_rate_by_bracket()
		self.net_pay = self.gross_pay - self.gross_pay * self.tax

    # Returns tax rate based on dependents bracket
	def get_tax_rate_by_bracket(self):
		if 0 <= self.dependents <= 1:
			return .25              # 0 - 1 | .25
		if self.dependents <= 3:
			return .20              # 2 - 3 | .20
		else:
			return .15              # 4 +   | .15

	def print_user_tax_info(self):
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
			sep="\n"
		)

if __name__ == "__main__":
	main()