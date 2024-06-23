# another way
name2 = str(input("Enter the string : \n"))
rev_str = name2[::-1] # [starting point:Ending point:step to start]
if name2 == rev_str:
    print(f"{name2} is Palindrome")
else:
    print(f"{name2} is not a Palindrome")


# or
original_str = "NAMAN"
def is_palindrome(original_str):
    rev_str = original_str[::-1]
    print(rev_str)
    if original_str == rev_str:
        print("Palindrome")
    else:
        print("It is not")


is_palindrome(original_str)