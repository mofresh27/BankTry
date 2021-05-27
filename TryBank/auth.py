
import random
import validation
import database
from getpass import getpass
import os




def init():
    print("Welcome to Tech Federal Credit Union")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    
    
    global account_number_from_user

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)
        # print(user)

        if user:
            
           
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")
   


    account_number = generation_account_number()


    is_user_created = database.create(account_number, first_name, last_name, email, password,)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Current Balance (5) exit \n"))

    if selected_option == 1:

        deposit_operation(user)

    elif selected_option == 2:

        withdrawal_operation(user)

    elif selected_option == 3:

        logout()
    
    elif selected_option == 4:
        set_current_balance(user)

    elif selected_option == 5:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    
    print("Your account balance is: %s" % user[4])
    withdraw = int(input("How much would you like to wiihdraw?\n"))
    new_balance = int(user[4])- withdraw
    

    if new_balance >= withdraw:
        print("Your account balance is: %d" % new_balance)
        user_record = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    
        user_db_path = "data/user_record/"
        f = open(user_db_path + str(account_number_from_user) + ".txt", "w")
        f.write(user_record[4])
        f.close()

        return bank_operation(user)
        
    else:
        print("Insuffienct funds")
        withdrawal_operation(user)

 


def deposit_operation(user):

    print("Your account balance is: %s" % user[4])
    deposit = int(input("How much would you like to deposit?\n"))
    new_balance = int(user[4])+ deposit
    print("Your account balance is: %d" % new_balance)
    user_record = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    
    user_db_path = "data/user_record/"
    f = open(user_db_path + str(account_number_from_user) + ".txt", "w")
    f.write(user_record[4])
    f.close()

    return bank_operation(user)

    
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user):
    new_balance = user[4]
    print("Your account balance is: %s" % new_balance)


def get_current_balance(user_details):
    return user_details[4]


def logout(user):
    os.remove(user)
    login()


init()
