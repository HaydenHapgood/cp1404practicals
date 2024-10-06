import random

print(random.randint(5, 20))  # line 1
# smallest = 5, largest = 20

print(random.randrange(3, 10, 2))  # line 2
# smallest = 3, largest = 9
# as the range is from 3 in steps of 2 to 10, a 4 is impossible.

print(random.uniform(2.5, 5.5))  # line 3
# smallest = 2.5, largest = 5.5

# Random number from 0 - 100 inclusive, example of 1-100 and 1-100 with 5 decimals
print(random.randint(1,100))
print(f'{random.uniform(1,100):,.5f}')