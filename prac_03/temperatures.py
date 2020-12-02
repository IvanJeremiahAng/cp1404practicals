"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    def tempcheck(choice):
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
        else:
            fahrenheit = float(input("Fareinheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:.2f} C".format(celsius))

        print("Thank you.")

    MENU = """C - Convert Celsius to Fahrenheit
            F - Convert Fahrenheit to Celsius
            Q - Quit"""
    print(MENU)
    choice = ""
    while choice != "Q":
        choice = input(">>> ").upper()
        tempcheck(choice)
        if choice != "Q" and choice != "C" and choice != "F":
            print("Invalid option")


main()
