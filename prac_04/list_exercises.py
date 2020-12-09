def main():
    num1 = int(input("Number: "))
    num2 = int(input("Number: "))
    num3 = int(input("Number: "))
    num4 = int(input("Number: "))
    num5 = int(input("Number: "))
    num_list = (num1, num2, num3, num4, num5)
    print("The first number is:", num1)
    print("The last number is:", num5)
    print("The smallest number is:", min(num_list))
    print("The largest number is:", max(num_list))
    print("the average of the number is:", (sum(num_list)) / 5)

    sernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                'BaseStdIn',
                'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("What is your username?: ")
    if username in sernames:
        print("Access granted")
    else:
        print("Access denied")


main()
