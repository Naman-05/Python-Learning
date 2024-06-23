# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24



number = int(input("Enter the number: "))
if number < 0:
    print("Factorial is not possible")
else:
    fact = 1
    for i in range (1,number+1):
        fact = fact * i
print(f'Factorial of {number} is {fact}')