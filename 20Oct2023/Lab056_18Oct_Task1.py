# Factorial

number = int(input("Enter the number: "))
if number < 0:
    print("Factorial is not possible")
else:
    fact = 1
    for i in range (1,number+1):
        fact = fact * i
print(f'Factorial of {number} is {fact}')
