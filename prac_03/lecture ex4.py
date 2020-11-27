"""
if age >= 65 then
    he/she will get 10 vouchers of face value $20 each
else if the person is between 55 inclusive and 65 years of age
    he/she will get 15 vouchers of face value $10 each
else
    he will get 20 vouchers of face value $5 each
end if
"""


def get_vouchers(age):
    if age >= 65:
        return 10, 20  # 10 vouchers of $20 each
    elif 55 <= age < 65:
        return 15, 10  # 15 vouchers of $10 each
    else:
        return 20, 5  # 20 vouchers of $5 each


def main():
    age = int(input("Enter your age: "))
    number_of_vouchers, voucher_value = get_vouchers(age)
    print("Number of vouchers:", number_of_vouchers)
    print("Value of each voucher:", voucher_value)


if __name__ == '__main__':
    main()
