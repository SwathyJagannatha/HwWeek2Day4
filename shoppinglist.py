#2. The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). 
#Task 2: Include a feature to remove items from the list. 
#Task 3: Add a function that prints out the entire list.

shopping_list = []

def add_item(shopping_list):
    item = input("What would you like to add to your shopping list? ")
    if item in shopping_list:
        print(f"Sorry the {item} already exists in your shopping list!")
    else:
        shopping_list.append(item)
    print(shopping_list)
    # check if item already exists and dont allow duplicates

def remove_item(shopping_list):
    item = input("Which item would you like to remove? ")
    if item in shopping_list:
        shopping_list.remove(item)
        print("List after removing item:")
        print(shopping_list)
    else:
        print(f"{item} is not in your shopping list...")
    print(shopping_list)

def print_item(shopping_list):
    if len(shopping_list) > 0:
        print("Here is your Shopping List:")
        print(shopping_list)
    else:
        print("Sorry, Your shopping list is empty! Try adding item to your list!")

# is responsible for driving my code
# this is where the while loop will live
# and it will also call all my other functions

def main(shopping_list):
    print("""
    Please choose from the list below:
          1. add an item to your inventory
          2. remove an item from your inventory
          3. print the entire shopping list
          4. quit
        """)
    while True:
        response = input("What would you like to do? ")
        # can also have the multi-line print here instead
        if response == "1":
            add_item(shopping_list)
        elif response == "2":
            remove_item(shopping_list)
        elif response == "3":
            print_item(shopping_list)
        elif response == "4":
            print("Be safe out there! Here's what you have")
            print(shopping_list)
            print("Exiting")
            break
        else: 
            print("Please choose a valid option 1 2 3 or 4")
    pass

main(shopping_list)