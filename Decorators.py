def decor(func):
    def wrap():
        print("<===============>")
        func()
        print("<===============>")
    return wrap

def print_text():
    print("Salutations World!")

decorated = decor(print_text)


def my_stars(func):
    def star():
        print("*************************")
        func()
        print("*************************")
        func()
        print("*************************")
    return star

def my_words():
    print("Didn't watch Star Wars")

decoration = my_stars(my_words)

@my_stars
def my_style():
    print("I am the worlds greatest Python Programmer!")

my_style();



















"""
Conclusion, from my understanding the first step we created a function
called decor. Next we described what the function within the function 
did which was called "wrap." The "wrap" function "wraps" whatever function
that specifies its use. In the example the next function "print_text" it
is designed to print a string. When a variable is assigned to a string it
specified the Decoration outside of the function that it used.
Next it outlined the varible with "()" next to it. There is no limit to how many
times the "func()" can be used in between the commands inside of a decoration function.

Generally they are functions that decorate other functions.

You can also substitute defining the decor function with an @(function name)
over the function that you want decorated. Then you select the function and put
a semi-colon after it. $function$();
"""