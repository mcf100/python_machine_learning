"""
Write a function that calculates the factorial of a number.

The factorial of a number is defined like this:

n! = n * (n-1) * (n-2) * (n-3) * ... 

e.g. 

3! = 3 * 2 * 1

The factorial of zero, 0!, is defined as 1.

"""

def factorial(value):
    
    result = 1 

    for i in range(2, value + 1):
        result = result * i
    return result

def main():
    result = factorial(int(input("Please input the number you want the factorial of > ")))

    print("Result:", result)

main()