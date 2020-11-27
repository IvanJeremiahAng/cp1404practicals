def main():
    temp1 = celcius_to_fahrenheit(10)
    # 10 & 1.8 + 32.0 = 50 -> temp1 = 50

    temp2 = celcius_to_fahrenheit(50)
    # 50* 1.8 + 32.0 = 122 -> temp2 = 122
    print(temp1)
    print(temp2)


def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32.0


if __name__ == '__main__':
    main()
