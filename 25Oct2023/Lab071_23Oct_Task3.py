# Create a Function with a Parameter which can do x^y

def powercalc(x,y):
    z=x**y
    return z
a = int(input("enter first number\n"))
b = int(input("enter second number\n"))
res = powercalc(a,b)
print (res)