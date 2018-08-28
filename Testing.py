import random

random_words = (["mysterious", "neighborhood", "occasionally", "pennsylvania", "independent", "mathematics", "remarkable"])
#random_word_count = word().count()

def(hangman_word):
#Here lets take a random word from the list 'random_words' and assign it to a variable.
    x = random_words
    secure_random = random.SystemRandom(choice.x)
    hangman_word = secure_random
    return hangman_word


def place_holders(x):
#Here
    x = hangman_word()
    for letter in x:
        letter.append(x)
        for char in x:
            print(list(x))
            x.append(y)
            def replace(y):
                new_text = ('_',)
                for c in y:
                    if c.isalpha():
                        new_text += '^'
                    else:
                        new_text += c
                return y
        place_holders.append(y)
    return place_holders(x)


print(hangman_word)





"""def get_random_word():
    for thing in random_words():
randrange
"""

