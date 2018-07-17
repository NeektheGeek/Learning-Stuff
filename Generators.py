##0 Remark
#Generators define a container that can produce a list one at a time
#You start by defining a function
def countdown():
    #Next you choose a string and what you want to print
    i = 100
    n = 50
    #Next you create a "While" statement with a yield command.
    #You want to specify how this string acts when it is called upon.
    while i > 0:
        yield i
        i -= 1
    while n < 501:
        yield n
        n += 50
        n <= 501

#Here you want to specify what string in what generator you want to use.

"""for ni in countdown():
    print(ni)"""
##1st Remark
"""def infinite_fours():
    while True:
        yield 7

for i in infinite_fours():
    print(i)"""
##2nd Remark
"""def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i"""

"""Here we are showing that generators can be shown as finite lists.
If we specify it as a list and choose the string as a variable that
can be chosen for later when we print it the variable it will limit
the generator to the specific variable."""

"""print(list(numbers(110)))"""
##3rd Remark
def make_word():
    word = ""
    for ch in "pneumonoultramicroscopicsilicovolcanoconiosis":
        word += ch
        yield word

print(list(make_word()))

"""
1. Generators can be infinite. As shown by the infinite_fours
function.
2. Infinite Generators can be specified as a infinite set of commands
within a finite list.
3. Generators can be produce about anything, in the 3rd section
the generator is produced to add a letter(character) into each line 
until it is completed. This can go on infinitely. 
Conclusion, You can produce multiple generators at once but
    I have not found a way to produce them side by side. You 
    can list them together which it will procude one then 
    the other in order of the listed but further testing is
    needed"""