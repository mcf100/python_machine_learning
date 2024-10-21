"""
The Fridge

Get the user to enter a temperature in celcius

< 0: Print "Fridge too cold"
0 - 4: Print "Fridge OK"
4 - 6: Print "Fridge too warm"
> 6: Print "Fridge broken"
"""

STATUS_TOO_COLD = "Fridge too cold"
STATUS_OK = "Fridge OK"
STATUS_TOO_WARM = "Fridge too warm"
STATUS_BROKEN = "Fridge is broken"

status = STATUS_BROKEN

temp = float(input("Please enter fridge temperature in celcius: "))

if temp < 0:
    status = STATUS_TOO_COLD
elif temp <= 4:
    status = STATUS_OK
elif temp <= 6:
    status = STATUS_TOO_WARM
else:
    status = STATUS_BROKEN

print(status)