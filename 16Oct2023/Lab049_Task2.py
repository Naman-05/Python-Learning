# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year


Year = int(input("Enter the Year: "))
# is_leap_year = False
# it is a default value

if(Year%4==0 and Year%100!=0) or (Year%400==0):
    is_leap_year = True
else:
    is_leap_year = False
print(f"{Year} is {is_leap_year}")