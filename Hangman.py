import random
import secrets
import time

"""name = input("What's your name?")
print("Well,", name, "Do you want to play Hangman?")

time.sleep(10)

print(name, "too bad, you're playing anyways :)")
"""
word = "secret"

guesses = '_'

correct_guesses = ()
incorrect_guesses = ()

def blank_lines():
    for letter in word:
        word.append()
        return "_"

turns = 10

random_words = (["mysterious", "neighborhood", "occasionally", "pennsylvania", "independent", "mathematics", "remarkable"])
""""
def Hangman_Words():
    secure_random = random.SystemRandom()
    print(secure_random.choice(random_words))
    return


while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, )
            print()
        else:
            print("_",)
            failed += 1
        if failed == 0:
            print("You won")
            break

        print()
        guess = input("guess a character:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", +  turns, 'more guesses')
            if turns == 0:
                print("You lose!")


print(Hangman_Words)
"""
"""print("---------\n|       |\n|       O\n|     / + \ \n|    |  |  |\n|    *  -  *\n|     /   \ \n|    |     |\n|   <       >")"""

print (blank_lines())
