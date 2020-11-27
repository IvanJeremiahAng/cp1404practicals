
def main():
    # counting odd numbers from 1 - 20
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    # counting in 10s from 0 - 100
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()

    # counting down from 20 - 1
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    # printing stars based on user input
    star = int(input("Enter the number of stars you want displayed: "))
    for i in range(star):
        print("*", end='')
    print()

    # printing stars on new lines
    for i in range(1, star + 1):
        print("*" * i)
    print()


main()
