import random


def main():
    print("Welcome! I am here to help you decide what to eat!")
    choice = get_choice()

    if choice == "eat":
        ...

    if choice == "add":
        ...

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
    ...


def three():
    ...


if __name__ == "__main__":
    main()
