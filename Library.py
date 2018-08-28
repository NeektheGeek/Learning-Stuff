a = [1, 3, 5]
b = a
a[:] = [x for x in a]
print(b)