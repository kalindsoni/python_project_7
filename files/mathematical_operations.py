import math

class mathematical_operation:

    def factorial_(self, num):
        if num == 0 or num == 1:
            return 1

        return num * self.factorial_(num - 1)

    def compound_interest(self, principal, rate, time):
        amount = principal * (1 + rate / 100) ** time
        return amount

    def trigonometric_calculation(self, angle):
        radians = math.radians(angle)
        sine = math.sin(radians)
        cosine = math.cos(radians)
        tangent = math.tan(radians)

        return sine, cosine, tangent

    def area_of_geometric_shapes(self, shape, *args):
        if shape == "circle":
            radius = args[0]
            area = math.pi * radius ** 2
            return area
        
        elif shape == "rectangle":
            length, width = args
            area = length * width
            return area

        elif shape == "triangle":
            base, height = args
            area = 0.5 * base * height
            return area

        else:
            print("Invalid shape. Supported shapes: circle, rectangle, triangle.")
            return None

    def back_to_main_menu(self):
        print("Returning to main menu...")

def maths():
    
    math_ops = mathematical_operation()
    while True:
        print("\n===== Mathematical Operations =====")
        print("1. Factorial")
        print("2. Compound interest")
        print("3. Trigonometric calculation")
        print("4. Area of geometric shapes")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            num = int(input("Enter a number: "))

            result = math_ops.factorial_(num)

            print(f"Factorial of {num} is: {result}")

        elif choice == "2":

            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter interest rate (%): "))
            years = float(input("Enter time in years: "))

            amount = math_ops.compound_interest(
                principal,
                rate,
                years
            )

            print(f"Compound amount: {amount}")

        elif choice == "3":

            angle = float(input("Enter angle in degrees: "))

            sine, cosine, tangent = (
                math_ops.trigonometric_calculation(angle)
            )

            print(f"Sine: {sine}")
            print(f"Cosine: {cosine}")
            print(f"Tangent: {tangent}")

        elif choice == "4":

            shape = input(
                "Enter shape (circle, rectangle, triangle): "
            ).lower()

            if shape == "circle":

                radius = float(input("Enter radius: "))

                area = math_ops.area_of_geometric_shapes(
                    shape,
                    radius
                )

                print(f"Area of circle: {area}")

            elif shape == "rectangle":

                length = float(input("Enter length: "))
                width = float(input("Enter width: "))

                area = math_ops.area_of_geometric_shapes(
                    shape,
                    length,
                    width
                )

                print(f"Area of rectangle: {area}")

            elif shape == "triangle":

                base = float(input("Enter base: "))
                height = float(input("Enter height: "))

                area = math_ops.area_of_geometric_shapes(
                    shape,
                    base,
                    height
                )

                print(f"Area of triangle: {area}")

            else:
                print("Invalid shape.")

        elif choice == "5":
            math_ops.back_to_main_menu()
            break

        else:
            print("Invalid choice.")



