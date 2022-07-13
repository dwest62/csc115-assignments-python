# Variables grade and isGrad are taken as std input.
# Grade is decremented by 11 points if user is a Graduate Student (we expect more).
# Program outputs Letter grade and corrosponding message.

grade = int(input("Enter grade (0-100): "))
isGrad = input("Graduate student (Y/N): ") in ("Y","y")
if isGrad:
	grade -= grade * .10

if 90 <= grade:
    print("Your letter grade is: A")
    print("Excellent!")
elif 80 <= grade <= 89:
    print("Your letter grade is: B")
    print("Excellent!")
elif 70 <= grade <= 79:
    print("Your letter grade is: C")
    "Could improve."
elif 50 <= grade <= 59:
    print("Your letter grade is: D")
    print("Could improve.")
else:
    print("Your letter grade is: F")
    print("Needs work.")