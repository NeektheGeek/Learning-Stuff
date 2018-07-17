import random
number = random.randint(1, 2)

name = input('Hi, Whats your name?')
print("Well,", name, "I am thinking of a number between 1 and 2, take a guess")

Yes = ["Yes", "Y", "y", "yeah", "ye", "YE", "yea", "YES", "yes"]
No = ["No", "no", "Nah", "Na", "nah", "na", "N", "n", "No Way"]
guess1 = int(input())
if guess1 == number:
    print("That is Correct!")
while guess1 != number:
    if guess1 < number:
        print("Too Low! Try Again!")
        guess1 = int(input())
    elif guess1 > number:
        print("Too High! Try Again!")
        guess1 = int(input())
    print("That is Correct!", name, "Do you want to play again?")
    answer = input("Yes or No?")
if dict[No] == input():
        print("Okay,", name,  "see you later!")
elif dict[Yes] == input():
        print("Okay,", name, "I am thinking of a number between 1 and 100")
