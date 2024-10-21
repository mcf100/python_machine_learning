"""
A default value defined for a parameter will come into play if there is no value provided in the argument. 
If you wish to provide a default value for a middle parameter then you must provide default values for every parameter 
after it
"""
def new_patient(name, type, age = -1):
    print(name, type, age)

def main():
    new_patient("Biffy", "dog", 5)
    new_patient("Tiddles", "cat")
    new_patient("Rover", "dog", 8)

    main()