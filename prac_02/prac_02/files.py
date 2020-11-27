# question 1
question1 = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=question1)
question1.close()

# question 2
question2 = open("name.txt", "r")
name = question2.read().strip()
print("The name you have entered is:", name)
question2.close()

# question 3
question3 = open("numbers.txt", "r")
num1 = int(question3.readline())
num2 = int(question3.readline())
print(num1 + num2)
question3.close()

# question 4
question4 = open("numbers.txt", "r")
total = 0
for i in question4:
    q4num = int(i)
    total += q4num
print(total)
question4.close()
