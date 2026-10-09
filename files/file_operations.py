class file_operations:

    def create_file(self, filename):
        with open(filename, "w") as file:
            print(f"\nFile '{filename}' created successfully.")

    def write_file(self, filename):

        text = input("Enter text to write: ")
        with open(filename, "w") as file:
            file.write(text)

        print("Text written successfully.")

    def append_file(self, filename):
        text = input("Enter text to append: ")

        with open(filename, "a") as file:
            file.write("\n" + text)

        print("Text appended successfully.")

    def read_file(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()

            print("\n----- File Content -----")
            print(content)
            print("------------------------")

        except FileNotFoundError:
            print("File does not exist.")

        finally:
            print("File reading operation completed successfully.")

    def back_to_main_menu(self):
        print("Returning to main menu...")

def FO():
    while True:
        file_ops = file_operations()


        print("\n===== File Operations =====")
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Append to a file")
        print("4. Read a file")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            filename = input("Enter filename: ")

            file_ops.create_file(filename)

        elif choice == "2":

            filename = input("Enter filename: ")

            file_ops.write_file(filename)

        elif choice == "3":

            filename = input("Enter filename: ")

            file_ops.append_file(filename)

        elif choice == "4":

            filename = input("Enter filename: ")

            file_ops.read_file(filename)

        elif choice == "5":

            file_ops.back_to_main_menu()
            break

        else:
            print("Invalid choice.")


