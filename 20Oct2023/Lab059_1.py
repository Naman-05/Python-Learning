# Grade Calculator

grade = int(input("Enter your Marks\n"))

match grade:
    case grade if grade > 100:
        print("Invalid Input")
    case grade if grade >= 90 and grade <= 100:
        print("your grade is A")
    case grade if grade >= 80 and grade <= 89:
        print("your grade is B")
    case grade if grade >= 70 and grade <= 79:
        print("your grade is C")
    case grade if grade >= 60 and grade <= 69:
        print("your grade is D")
    case _:
        print("your grade is F")
