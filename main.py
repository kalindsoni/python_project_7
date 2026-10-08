from files.datetime_operations import datetime
from files.mathematical_operations import mathematical_operation
from files.random_data import random_data_generation
from files.unique_identifier import unique_identifier
from files.file_operations import file_operations
from files.module_explorer import module_explorer


# def date_time_menu():

#     toolkit = MultiUtilityToolkit()

# def mathematics_menu():

#     math_ops = mathematical_operation()


# def random_menu():

#     random_gen = random_data_generation()


# def uuid_menu():

#     uuid_gen = unique_identifier()


# def file_menu():

#     file_ops = file_operations()


# def module_menu():

#     explorer = module_explorer()




# if __name__ == "__main__":

while True:

    print("\n==============================")
    print("Welcome to Multi-Utility Toolkit")
    print("==============================")

    print("1. Date/time operations")
    print("2. Mathematical operations")
    print("3. Random data generation")
    print("4. Generate UUID")
    print("5. File operations")
    print("6. Explore module attributes")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    match choice:

        case 1:
            datetime()

        case 2:
            mathematical_operation()

        case 3:
            random_data_generation()

        case 4:
            unique_identifier()

        case 5:
            file_operations()

        case 6:
            module_explorer()

        case 7:
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")