def main():
    days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

    days[0:3] = []
    print(days)

    days.remove("Sat")
    print(days)

    days.pop(0)
    print(days)

    item = days.pop(0)
    print(days)
    print(item)

    del days[0]
    print(days)

    days.append("Thursday")
    print(days)

    days.clear()
    print(days)


main()