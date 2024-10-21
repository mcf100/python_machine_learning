def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    print(fruits["apple"])
    print(fruits["orange"])
    print(fruits["banana"])

    months = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
    }

    months["Apr"] = "April"

    months.update({"May":"May", "Jun":"June"})
    print(months)


main()

