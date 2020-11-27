
def main():
    items = int(input("Number of items: "))
    total_price = 0
    while items < 0:
        print("Invalid amount of items.")
        items = int(input("Number of items: "))

    for i in range(items):
        price = float(input("Price of item:: "))
        total_price += price

    if total_price > 100:
        discount = total_price * 0.9
        print("Total price for " + str(items) + " items is $" + str(discount))
    else:
        print("Total price for " + str(items) + " items is $" + str(total_price))


main()
