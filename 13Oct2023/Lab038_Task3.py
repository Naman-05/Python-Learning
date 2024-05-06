# 1. Use the ternary operator to find the maximum of three numbers entered by the user.

a=input("Enter number1 \n")
b=input("Enter number2 \n")
c=input("Enter number3 \n")

max_number = a if a>b and a>c else b if b>a and b>c else c
print("maximum number of",a,b,c,"is:", max_number )


# 2. Develop a Python script that calculates the square and cube of a given number.
num = int(input("Enter a number:"))
square = num ** 2
cube = num ** 3
print("Square of a number is:",square)
print("Cube of a number is:",cube)
