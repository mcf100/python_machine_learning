"""
The Fridge

Get the user to enter a temperature in celcius

< 0: Print "Fridge too cold"
0 - 4: Print "Fridge OK"
4 - 6: Print "Fridge too warm"
> 6: Print "Fridge broken"
"""

temp = float(input("Please enter fridge temperature in celcius: "))

if temp < 0:
    print("Fridge too cold")
elif temp <= 4:
    print("Fridge OK")
elif temp <= 6:
    print("Fridge too warm")
else:
    print("Fridge is broken")