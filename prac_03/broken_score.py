"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():

    def scorecheck(score):
        if score < 0 or score > 100:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")

    userscore = float(input("Enter score: "))
    scorecheck(userscore)

main()
