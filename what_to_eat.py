import random, sys
from os.path import exists


def main():
    print("\n    Welcome! I am here to help you decide what to eat!")
    print("   ====================================================\n")
    choice = get_choice()

    if choice == "eat":
        food_to_eat = get_food()
        print(f"\n    Today you should eat: {food_to_eat}")


    if choice == "add":
        new_food = input("\nName of the dish that you want to save: ").strip().capitalize()
        save_food(new_food)

    if choice == "del":
        print("This option is not implemented yet")

    print("\nThank you, see you again!")
    print("=========================")


def get_choice():
    """
    Asks the user for input in a loop, returns a choice string only if the input is valid
    """
    while True:
        choice = input("Would you like to eat something or add a new item to the list of your favorite dishes? (eat/add): ")
        if choice in ["eat", "add", "del"]:
            return choice


def get_food():

    # check if file exists
    if not exists("foodlist.txt"):
        sys.exit("No favorite food registered yet. Try again.")

    # open file and return one random dish name
    with open("foodlist.txt") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


def save_food(food_name):

    with open("foodlist.txt", "a") as file:
        file.write(f"{food_name}\n")
    


if __name__ == "__main__":
    main()
