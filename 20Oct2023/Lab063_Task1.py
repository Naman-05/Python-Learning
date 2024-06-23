# Palindrome Checker:
# Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
#
# Example - pramod
# madam - reverse(madam) -> same
# Naman -> reverse -> same
# Malayalam


# My Code
# With a built in Function
name = str(input("Enter the name : \n"))
name1 = "".join(reversed(name))
if name1 == name:
    print(f"{name} is Palindrome")
else:
    print(f"{name} is not a Palindrome")


# another way
name2 = str(input("Enter the string : \n"))
rev_str = name2[::-1] # [starting point:Ending point:step to start]
if name2 == rev_str:
    print(f"{name2} is Palindrome")
else:
    print(f"{name2} is not a Palindrome")

