# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)

r = int(input("Enter the Radius of Circle:\n"))
pi = 3.14
area=pi*(r**2)
print(area)



# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.

n1 = input("Enter Number1: \n")
n2 = input("Enter Number2: \n")

if n1>n2:
    print("Number1 is greater than Number2")
elif n1<n2:
    print("Number2 is greater than Number1")
else:
    print("Number1 and Number2 are Equal")

