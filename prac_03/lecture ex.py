min_age = 0
max_age = 150
valid_age = False
while not valid_age:
    try:
        age = int(input("Enter your age: "))
        if min_age <= age <= max_age:
            valid_age = True
        else:
            print("Age must be 0 - 150 inclusive.")
    except ValueError as e:
        print("Age must be an integer")
if age % 2:
    print("Your age is odd")
else:
    print("Your age is even")
    print("You are {} years old this year and will be {} next year.".format(age, age + 1))
