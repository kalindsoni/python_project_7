import random

class random_data_generation:

    def generate_random_number(self, start , end):
        return random.randint(start, end)

    def generate_random_list(self):
        random_list = [random.randint(1, 100) for i in range(10)]
        print("Random list:", random_list)

    def generate_random_passward(self, length):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        password = characters.join(random.choice(characters) for i in range(length))
        return password
    
    def generate_random_OTP(self):
        otp = random.randint(100000, 999999)
        return otp

    def back_to_main_menu(self):
        print("Returning to main menu...")

    def RD():
        while True:



            print("\n===== Random Data Generation =====")
            print("1. Generate random number")
            print("2. Generate random list")
            print("3. Generate random password")
            print("4. Generate random OTP")
            print("5. Back to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":

                start = int(input("Enter start range: "))
                end = int(input("Enter end range: "))

                number = random_gen.generate_random_number(
                    start,
                    end
                )

                print("Random number:", number)

            elif choice == "2":
                random_gen.generate_random_list()

            elif choice == "3":

                length = int(input("Enter password length: "))

                password = random_gen.generate_random_password(
                    length
                )

                print("Generated password:", password)

            elif choice == "4":

                otp = random_gen.generate_random_OTP()

                print("Generated OTP:", otp)

            elif choice == "5":

                random_gen.back_to_main_menu()
                break

            else:
                print("Invalid choice.")

random_gen = random_data_generation()