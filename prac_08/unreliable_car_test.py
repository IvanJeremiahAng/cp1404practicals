from prac_08.unreliable_car import UnreliableCar


def main():
    working = UnreliableCar("Working Car", 100, 99)
    breakdown = UnreliableCar("Suspiciously Shoddy Car", 100, 7)

    for i in range(1, 12):
        print("Driving {}km...".format(i))
        print("{:12} has driven {:2} km".format(working.name, working.drive(i)))
        print("{:12} has driven {:2} km".format(breakdown.name, breakdown.drive(i)))

    print(working)
    print(breakdown)


main()
