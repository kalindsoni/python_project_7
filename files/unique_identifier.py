import uuid

class unique_identifier:

    def generate_uuid(self):
        unique_id = uuid.uuid4()
        print(unique_id)

    def back_to_main_menu(self):
        print("Returning to main menu...")

def UI():
    while True:
        uuid_gen = unique_identifier()


        print("\n===== UUID Generator =====")
        print("1. Generate UUID")
        print("2. Back to main menu")

        choice = input("Enter your choice: ")


        if choice == "1":

            unique_id = uuid_gen.generate_uuid()

            print("Generated UUID:", unique_id)

        elif choice == "2":

            back_menu = uuid_gen.back_to_main_menu()
            break

        else:
            print("Invalid choice.")
