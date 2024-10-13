import random

number_of_quickpicks = int(input('How many quick picks would you like to generate: '))

quickpicks = []
for i in range(number_of_quickpicks):
    line = []
    while len(line) < 6:
        line.append(random.randint(1 , 45))
    quickpicks.append(line)

for pick in quickpicks:
    print(' '.join(map(str, pick)))