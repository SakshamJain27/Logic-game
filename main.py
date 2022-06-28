import random
import time

case1 = random.randint(1, 5)
case2 = random.randint(1, 5)
case3 = random.randint(1, 5)
case4 = random.randint(1, 5)

def printExample(caseItem, random_int):
    print(f"The first number is {caseItem}")
    print(f"The second number is {caseItem}")
    print(f"The third number is {random_int}")
    print("There solution is:", caseItem*caseItem-random_int)
    print("\n")
    time.sleep(3)


def askUser(caseItem, random_int):
    print(f"The first number is {caseItem}")
    print(f"The second number is {caseItem}")
    print(f"The third number is {random_int}")
    userChoice = int(input("Enter the solution:"))
    total = (caseItem*caseItem-random_int)
    if userChoice == total:
        print("Yes you guessed it")
    else:
        print("Sorry, you are wrong, it was", total)


printExample(case1, random.randint(1, 10))
printExample(case2, random.randint(1, 10))
printExample(case4, random.randint(1, 10))
askUser(case4, random.randint(1, 10))
