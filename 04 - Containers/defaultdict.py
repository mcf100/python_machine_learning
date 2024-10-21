from collections import defaultdict

def main():
    people = defaultdict(int)
    
    people.update({"Bob": 45, "Sarah": 30})

    print(people)

    print(people["Bob"])
    print(people["Vicky"])

main()