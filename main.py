from files.datetime_operations import Dtime
from files.mathematical_operations import maths
from files.random_data import RD
from files.unique_identifier import Random
from files.file_operations import FOperation
from files.module_explorer import Module


if __name__ == "__main__":

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

        choice = int(input("Enter your choice (1-7): "))

        match choice:

            case 1:
                Dtime()
            case 2:
                maths()

            case 3:
                Random()

            case 4:
                UI()

            case 5:
                FOperation()

            case 6:
                Module()

            case 7:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice.")
