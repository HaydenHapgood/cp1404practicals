name_file = open('name.txt', 'w')
name = input('What is your name? : ')
print(name, file=name_file)
name_file.close()

name_file = open('name.txt', 'r')
read_name = name_file.read().strip()
name_file.close()
print(f'Hi {read_name}!')

total_number = 0
with open('numbers.txt', 'r') as numbers_file:
    for i in range(2):
        number = numbers_file.readline().strip()
        total_number += int(number)
    print(total_number)

total_sum = 0
with open('numbers.txt', 'r') as numbers_file:
    for line in numbers_file:
        total_sum += int(line)
    print(total_sum)