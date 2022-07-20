# This program calculates the user's net pay based on their tax bracket.
# It accepts std inputs for first name, last name, monthly gross pay, and number of dependants.
# After calculation, program prints user info: name, gross pay,["money"] dependents, tax rate, and net pay.

def main():
    name = read_name()
    gross_pay = read_gross_pay()
    dependents = read_dependents()
    rate = compute_tax_rate(dependents)
    net_pay = compute_net_pay(gross_pay, rate)
    fmt = FormatString
    w = 12
    print (
        "",
        f"{fmt.to_text_block('Name:', w)}{name}",
        f"{fmt.to_text_block('Gross pay:', w)}{fmt.to_money(gross_pay)}",
        f"{fmt.to_text_block('Dependents:', w)}{dependents}",
        f"{fmt.to_text_block('Tax rate:', w)}{fmt.to_percent(rate)}",
        f"{fmt.to_text_block('Net Pay:', w)}{fmt.to_money(net_pay)}",
        "",
        sep="\n"
    )

def read_name() -> str:
    return input("Enter your name: ")

def read_gross_pay() -> float:
    return float(input("Enter your gross pay: "))

def read_dependents() -> int:
    return int(input("Enter your number of dependants: "))

def compute_tax_rate(dependents) -> float:
    if 0 <= dependents <= 1:
        return .25              # 0 - 1 | .25
    elif dependents <= 3:
        return .20              # 2 - 3 | .20
    else:
        return .15              # 4 +   | .15

def compute_net_pay(gross_pay, rate) -> float:
    return gross_pay - gross_pay * rate


class FormatString:
    @staticmethod
    def to_money(s: str) -> str:
        return f"${s:,.2f}"

    @staticmethod
    def to_percent(f: float) -> str:
        f *= 100
        return f"{f:.0f}%"

    @staticmethod
    def to_text_block(s: str, block_width: int) -> str:
        return f"{s:{block_width}}"

if __name__ == "__main__":
    main()