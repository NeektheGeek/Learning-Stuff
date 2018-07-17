union = {1, 2, 3, 4, 5, 6}
union2 = {4, 5, 6, 7, 8, 9}
intersection = {3, 6, 9, 12, 15}
intersection2 = {3, 6, 9, 12, 15}
difference = {5, 10, 15, 20, 25}
difference2 = {30, 35, 40, 45, 50}
symmetric_operator = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
symmetric_operator2 = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print(union | union2)
print(intersection & intersection2)
print(difference - difference2)
print(difference2 - difference)
print(symmetric_operator ^ symmetric_operator2)
print(symmetric_operator2 ^ symmetric_operator2)
print(union ^ union2)
"""
Unions - This operator will bring a set together.
intersection - This operator will only print items in both
difference - This operator will only print items in the first set
symmetric difference - This operator will print the items that are
different in the sets.
Conclusion, 
"""
