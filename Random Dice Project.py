def roll_dice1():
    print("---------------------------")
    if num1 == 1:
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|             O            |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
    if num1 == 2:
         print("| O                        |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                        O |")
    if num1 == 3:
         print("| O                        |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|             O            |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                        O |")
    if num1 == 4:
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
    if num1 == 5:
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|             O            |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
    if num1 == 6:
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
    print("---------------------------")

def roll_dice2():
    print("---------------------------")
    if num2 == 1:
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|             O            |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
    if num2 == 2:
         print("| O                        |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                        O |")
    if num2 == 3:
         print("| O                        |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|             O            |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                        O |")
    if num2 == 4:
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
    if num2 == 5:
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("|             O            |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
    if num2 == 6:
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
         print("|                          |")
         print("|                          |")
         print("|                          |")
         print("| O                      O |")
    print("---------------------------")
    print("You Rolled", num1 + num2)
    if num1 is num2:
        print("You Rolled Doubles!")
    if num1 + num2 is 2:
        print("You Rolled Snake-Eyes!")
    print("Would you like to roll again?")

import random

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
roll_dice1()
roll_dice2()


