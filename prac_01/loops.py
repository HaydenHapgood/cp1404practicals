print("Example:", end=' ')
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#Question a
print("a)", end=' ')
for i in range(0, 110, 10):
    print(i , end=' ')
print()

#Question b
print("b)", end=' ')
for i in range(20, 1, -1):
    print(i, end=' ')
print()

#Question c
stars = int(input("Enter number of stars: ", ))
print("c)", end=' ')
for i in range(0, stars):
    print("*", end='')
print()

#Question d
print("d)", end=' ')
for i in range(0, stars+1):
    print("*" * i)
print()
