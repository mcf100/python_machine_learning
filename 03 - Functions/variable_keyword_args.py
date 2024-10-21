
def add_description(**description):

    for property in description:
        print(property, ": ", description[property])
    
    print()

def main():
    add_description(height=180, weight=90, eyes="blue")
    add_description(trouser="black", beard=True)
    add_description(sex="male", height=170)
main()