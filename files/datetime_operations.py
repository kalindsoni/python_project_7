import datetime
import time

class MultiUtilityToolkit:

    def __init__(self):
        self.time = datetime.datetime.now()

    def current_time(self):
        now = datetime.datetime.now()
        print("Current date and time:", now)

    def difference_between_dates(self, date1, date2):
        d1 = datetime.datetime.strptime(date1)
        d2 = datetime.datetime.strptime(date2)
        delta = d2 - d1

        print("Difference between dates:", delta.days, "days")

    def format_date(self, date):
        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        print("Formatted date:", formatted_date)

    def stopwatch(self):

        start_time = datetime.datetime.now()
        input("Press Enter to stop the stopwatch...")
        end_time = datetime.datetime.now()
        elapsed_time = end_time - start_time

        print("Elapsed time:", elapsed_time)

    def countdown(self):
        seconds = int(input("Enter countdown time in seconds: "))

        while seconds > 0:
            print("Time remaining:", seconds)
            time.sleep(1)
            seconds -= 1

        print("Time's up!")

    def back_to_main_menu(self):
        print("Returning to main menu...")

class datetime:
    def Dtime():
        while True:
            toolkit = MultiUtilityToolkit()

            print("\n===== Date/Time Operations =====")
            print("1. Current date and time")
            print("2. Difference between two dates")
            print("3. Format a date")
            print("4. Stopwatch")
            print("5. Countdown timer")
            print("6. Back to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                toolkit.current_time()

            elif choice == "2":
                date1 = input("Enter first date (YYYY-MM-DD): ")
                date2 = input("Enter second date (YYYY-MM-DD): ")

                toolkit.difference_between_dates(date1, date2)

            elif choice == "3":
                date = input("Enter date (YYYY-MM-DD): ")
                toolkit.format_date(date)

            elif choice == "4":
                toolkit.stopwatch()

            elif choice == "5":
                toolkit.countdown()

            elif choice == "6":
                toolkit.back_to_main_menu()
                break

            else:
                print("Invalid choice.")

# https://github.com/Pushkar765/Moduler-Packakeger.py.git