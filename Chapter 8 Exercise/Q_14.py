"""
Use a list comprehension to produce a list that consists of all palindromic numbers between
100 and 1000.
"""

L = [num for num in range(100, 1001) if num == int(str(num)[::-1])]

print(f'\nThere are {len(L)} numbers that are a palindromic.\n')
print(L)
