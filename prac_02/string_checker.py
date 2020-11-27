
name = input("Enter you name: ").strip()

while name == "":
    print("Name cannot be empty!")
    name = input("Enter you name: ").strip()

print("Hi {}! Nice to meet you finally!".format(name.title()))

