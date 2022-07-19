# Variables grade and isGrad are taken as std input.
# Grade is decremented by 10 points if user is a Graduate Student (we expect more).
# Program outputs Letter grade and corrosponding message.
 
from enum import Enum

# Define grade range and message details
class LetterGrade(Enum):
	A = (90, 100) # (min, max)
	B = (80, 89)
	C = (70, 79)
	D = (60, 69)
	F = (0, 59)

LetterGrade.A.msg = LetterGrade.B.msg = "Excellent!"
LetterGrade.C.msg = LetterGrade.D.msg = "Could improve."
LetterGrade.F.msg = "Needs work."

# Get user inputed grade. Get graduate status.
grade = int(input("Enter grade (0-100): "))
isGrad = input("Graduate student (Y/N): ") in ("Y", "y")

# Grade is reduced by 10% if user is graduate
if isGrad:
	grade -= grade * .10

# Match letter with grade and print corrosponding letter name and message.
for letter in LetterGrade:
	if letter.value[0] <= grade <= letter.value[1]: # grade between (min, max) inclusive
		print(f"Your letter grade is: {letter.name}")
		print(letter.msg)
		exit() # match found -> no need to continue