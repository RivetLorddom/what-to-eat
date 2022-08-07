import random, sys
from os.path import exists


def main():
    print("Welcome! I am here to help you decide what to eat!")
    choice = get_choice()

    if choice == "eat":
        get_food()

    if choice == "add":
        new_food = input("Name of the food that you want to save: ")
        save_food(new_food)

    if choice == "del":
        ...

    print(random.randint(1, 100))


def get_choice():
    """
    Asks the user for input in a loop, returns a choice string only if the input is valid
    """
    while True:
        choice = input("Would you like to eat something or add a new item to you list of your favorite foods? (eat/add): ")
        if choice in ["eat", "add", "del"]:
            return choice


def get_food():

    # check if file exists
    if not exists("foodlist.txt"):
        sys.exit("No favorite food registered yet. Try again.")

    # open file
    with open("foodlist.txt") as file:
        ...


def save_food(food_name):
    with open("foodlist.txt", "a") as file:
        file.write(food_name)
    


if __name__ == "__main__":
    main()
