"""

Write a function that asks the user to enter their weight in kilos and their height in meters, then calculates their BMI.

weight / (height * height)

The function should return all three values

"""
def bmi_calc():
    weight = input("Please enter your weight in kilos > ")
    height = input("Please enter your height in meters > ")
    
    weight = float(weight)
    height = float(height)
    
    bmi = weight / (height * height)

    return weight, height, bmi


def main():
    weight, height, bmi = bmi_calc()
    print("Weight: ", weight)
    print("Height: ", height) 
    print("BMI: ", bmi)

main()