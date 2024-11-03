minlength = 5
password = ""


def get_password():
    global password
    while len(password) < minlength:
        password = input('Enter password: ')
        if len(password) < minlength:
            print('Password is too short, please try again.')


get_password()


def print_password():
    for i in range(len(password)):
        print('*', end=" ")
    print()


print_password()