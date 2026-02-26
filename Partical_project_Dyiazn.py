# Python Practice Toolkit Project
# Covers loops, functions, lists, dictionaries, libraries, user input

import datetime
import os
import random
import math
import sys


# dictionary to store users
users = {}


# function 1: register user
def register():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    users[name] = age

    print("✅ User registered successfully")


# function 2: view users
def view_users():
    if not users:
        print("No users found")
        return

    print("\nRegistered Users:")
    for name, age in users.items():
        print(f"Name: {name}, Age: {age}")


# function 3: random number generator
def random_number():
    num = random.randint(1, 100)
    print("🎲 Random number:", num)


# function 4: square root calculator
def square_root():
    number = float(input("Enter number: "))
    print("Square root is:", math.sqrt(number))


# function 5: show date and time
def show_time():
    print("Current date and time:")
    print(datetime.datetime.now())


# function 6: show current directory
def show_directory():
    print("Current directory:")
    print(os.getcwd())


# function 7: coding practice problem (even numbers)
def even_numbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    print("Even numbers are:")
    for n in numbers:
        if n % 2 == 0:
            print(n)


# main menu loop
while True:

    print("\n===== Python Practice Toolkit =====")
    print("1. Register User")
    print("2. View Users")
    print("3. Generate Random Number")
    print("4. Square Root Calculator")
    print("5. Show Date and Time")
    print("6. Show Current Directory")
    print("7. Show Even Numbers")
    print("8. Show Python Version")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        view_users()

    elif choice == "3":
        random_number()

    elif choice == "4":
        square_root()

    elif choice == "5":
        show_time()

    elif choice == "6":
        show_directory()

    elif choice == "7":
        even_numbers()

    elif choice == "8":
        print(sys.version)

    elif choice == "9":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")