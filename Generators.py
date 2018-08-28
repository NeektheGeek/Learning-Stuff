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



"""print(list(numbers(110)))"""
##3rd Remark
def make_word():
    word = ""
    for ch in "pneumonoultramicroscopicsilicovolcanoconiosis":
        word += ch
        yield word

print(list(make_word()))

