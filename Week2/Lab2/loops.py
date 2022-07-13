# Written for CSC 115 Lab 2
from random import randrange

def main():
    problems = [p1, p2, p3, p4]
    for i, func in enumerate(problems):
        print(f"\nProblem #{i + 1}")
        func()
    print()

def p1():
    start, stop, step = -10, 111, 10
    for i in range(start, stop, step):
        print(i)

def p2():
    i = 10
    sum = 0
    for _ in range(i):
        sum += randrange(0, 550, 2)
    avg = sum / i
    print(avg)

gip = lambda: input("say something: ")

def p3():
    ip = gip()
    while True:
        print(f"You said: {ip}")
        ip = gip()
        if ip == "done":
            break
    print("Goodbye!")

def p4():
    ip = gip()
    while ip != "done":
        print(f"You said: {ip}")
        ip = gip()
    print("Goodbye!")

if __name__ == "__main__":
    main()