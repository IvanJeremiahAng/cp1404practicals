import random


def main():
    line_num = 6
    minimum = 1
    maximum = 45

    quick_picks = int(input("How many quick picks do you want to generate?: "))

    for picks in range(quick_picks):
        quick_pick = []
        for lines in range(line_num):
            random_number = random.randint(minimum, maximum)
            while random_number in quick_pick:
                random_number = random.randint(minimum, maximum)
            quick_pick.append(random_number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
