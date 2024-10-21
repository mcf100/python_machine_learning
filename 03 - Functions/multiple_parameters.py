"""
Volume of box = width * height * length
"""

def calc_box_vol(width, height, length):
    return width * height * length

def main():
    how_wide = int(input("Input width: "))
    how_tall = int(input("Input height: "))
    how_long = int(input("Input length: "))

    volume = calc_box_vol(how_wide, how_tall, how_long) 

    print("Box volume is:", volume)

main()

