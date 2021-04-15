import datetime
import random

date = datetime.datetime.now()
allowed_users = ['Ifeoluwa', 'Seyi', 'Mike']
allowed_password = ['passwordifeoluwa', 'passwordseyi', 'passwordmike']
accout_number = []


def gen_acc_num():
    return random.randint(1000000000, 9999999999)


def login():
    name = input("What is your name: \n")

    if name in allowed_users:
        password = input("Your Password: \n")
        user_id = allowed_users.index(name)

        if password == allowed_password[user_id]:
            options(name, user_id)

        else:
            print('Password is incorrect, please try again')
            login()

    else:
        print('Name not found, please try again')
        login()


def register():
    print('Please fill the form below to Register')
    name = input('Name: ')
    password = input('Password: ')
    retype = input('Retype Password: ')

    if password == retype:
        allowed_password.append(password)
        allowed_users.append(name)
        accout_number.append(gen_acc_num())
        options(name, allowed_password.index(password))
    else:
        print('Password mismatch')
        register()


def bankOperations():
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    selected_option = int(input('Please select an option: '))

    if selected_option == 1:
        withdraw_amount = input(
            f"How much would you like to withdraw? #")
        print(
            f"Take your cash, you withdrew {withdraw_amount}. \nThank you for banking with us. \n\n")
        bankOperations()

    elif selected_option == 2:
        deposit_amount = input(
            f"How much would you like to deposit? #")
        print(
            f"Current Balance {deposit_amount}. \nThank you for banking with us. \n\n")
        bankOperations()

    elif selected_option == 3:
        complaint = input('What issue would you like to report: \n')
        print("Thank you for contacting us. \n\n")
        bankOperations()

    elif selected_option == 4:
        exit()

    else:
        print('Invalid Option selected, please try again. \n\n')
        bankOperations()


def options(name, id):
    print(f'Date: {date}')
    print('\n')
    print(f'Welcome {name}, your account number is {accout_number[id]}')

    bankOperations()


def atm():
    for i in range(len(allowed_users)):
        accout_number.append(gen_acc_num())

    mode = input('Login (L) or Register (R): ').upper()

    if mode == 'L':
        login()
    elif mode == 'R':
        register()
    else:
        print('Invalid Response')


atm()
