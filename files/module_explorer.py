class module_explorer:

    def explore_module_attributes(self, module_name):
        try:
            module = __import__(module_name)
            attributes = dir(module)

            print(f"\nAttributes of module {module_name}:")
            for i in attributes:
                print(i)

        except ImportError:
            print(f"Module '{module_name}' not found.")

        finally:
            print("Module exploration completed successfully.")

    def back_to_main_menu(self):
        print("Returning to main menu...")

    def ME():

        while True:

            print("\n===== Module Explorer =====")
            print("1. Explore module attributes")
            print("2. Back to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":

                module_name = input("Enter module name: ")

                explorer.explore_module_attributes(
                    module_name
                )

            elif choice == "2":

                explorer.back_to_main_menu()
                break

            else:
                print("Invalid choice.")

explorer = module_explorer()