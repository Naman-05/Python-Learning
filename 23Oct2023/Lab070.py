original_str = "naman"
reverse_str = lambda original_str : original_str[::-1]


if reverse_str("naman") == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")



add = lambda x,y : x+y

print(add(3,4))

a = lambda :input("Enter a Number ")
print(a**3)