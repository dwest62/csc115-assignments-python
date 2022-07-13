# This program calculates the user's net pay based on their tax bracket.
# It accepts std inputs for first name, last name, monthly gross pay, and number of dependants.
# After calculation, program prints user info: name, gross pay,["money"] dependents, tax rate, and net pay.

def main():
    fname, lname, gross, deps = get_user_info()
    tax = get_bracket(deps)
    net = calc_net_pay(gross, tax)

    user_info = {
        'Name': f"{fname} {lname}",
        'Gross pay': get_money_str(gross),
        'Dependents': deps,
        'Tax rate': get_tax_str(tax),
        'Net Pay': get_money_str(net)
    }

    for key, value in user_info.items():
        description = "{:12}".format(key)
        print(description, value)

def get_bracket(dependents):  # bracket | rate
    if 0 <= dependents <= 1:
        return .25              # 0 - 1 | .25
    if dependents <= 3:
        return .20              # 2 - 3 | .20
    else:
        return .15              # 4 +   | .15


def get_user_info():
    first_name = input("\nEnter your first name: ")
    last_name = input("Enter your last name: ")
    gross_pay = float(input("Enter your gross pay: "))
    dependants = int(input("Enter number of dependents: "))
    return (first_name, last_name, gross_pay, dependants)

def calc_net_pay(gross_pay, tax):
    return gross_pay - gross_pay * tax

def get_money_str(money):
    return "$" + "{:,.2f}".format(money)

def get_tax_str(tax):
    return "{:.0f}".format(tax * 00) + "%"

def print_user_info(user_info):
    for key, value in user_info.items():
        description = "{:12}".format(key)
        print(description, value)

if __name__ == "__main__":
    main()