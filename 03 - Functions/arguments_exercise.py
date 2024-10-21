"""
Exercise: 

Define a single function the accepts:
    one or more positional arguments
    zero or more variable arguments
    zero or more variable keyword arguments

    Make the function print out all the arguments it receives

"""

def description(name, *personality_attributes, **physical_attributes):
    print(name)
    
    print()
    
    for personality_attribute in personality_attributes:
        print(personality_attribute)
    
    print()
    
    for property in physical_attributes:
        print(property, ": ", physical_attributes[property])

def main():
    description("Max", "funny", "kind", "dopey", height=189, eyes="brown", hair="brown")

main()