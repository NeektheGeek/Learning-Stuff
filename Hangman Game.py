import random

#Dictionary of words
words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]


hangman = (
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  -+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    d-----
    |   |
    |   0
    | /-+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    ||  |  |
    |
    |   
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    ||  |  |
    |   | 
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    ||  |  |
    |   | 
    |  |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    ||  |  |
    |   | 
    |  | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    ||  |  |
    |   | 
    |  | | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    ||  |  |
    |   | 
    |  | | 
    |  | | 
    | -* *-
    --------
    """
)
random_word = random.choice(words)
random_word_length = len(random_word)
blank_char = (random_word_length * "_ ")
positive_answer = ("Yes", "y", "Y", "yes", "Ye", "ye", "yeah", "Yeah")
negative_answer = ("No", "N", "no", "n", "na", "nah", "nope", "negative")
correct_letters = []
incorrect_letters = []




def random_word_character_replace():
    for w in random_word:
        print(w, len(w))
        blank_char.append(len(w) * "_")
        return blank_char

#The actual program
def game_of_hangman():
    #Prompting user for name
    user_name = input("What's your name?")
    #Prompting user for answer
    first_questions = input("Well,", user_name, "would you like to play Hangman?", "Yes? or No")
    #Taking the user's answer and either running the program or ending it in a loop.
    while first_questions is ("Yes"):
        #Turns
        turns == 11
        guessed_letter = input("Guess a letter", user_name, "!")
        random_word.count(guessed_letter)
        if random_word.count() > 0:
            correct_letters.append(guessed_letter)
            turns += 0
        else:
            incorrect_letters.append(guessed_letter)
            turns += -1
            print(hangman += 1)
    while first_questions == ("No"):
        break

print (game_of_hangman())



