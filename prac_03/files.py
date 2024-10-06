name_file = open('name.txt', 'w')
name = input('What is your name? : ')
print(name, file=name_file)
name_file.close()

name_file = open('name.txt', 'r')
read_name = name_file.read().strip()
name_file.close()
print(f'Hi {read_name}!')

