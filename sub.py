def subject (math, eco, bio, phy, eng):
    total = math + eco + bio + phy + eng
    return total

def submark():
    sub1 = int(input("Enter marks of the first subject:"))
    sub2 = int(input("Enter marks of the secound subject:"))
    sub3 = int(input("Enter marks of the third subject:"))
    sub4 = int(input("Enter marks of the forth subject:"))
    sub5 = int(input("Enter marks of the fifth subject:"))

    marks = subject (sub1,sub2,sub3,sub4,sub5)
    print("Total marks:", marks)

    percentage = (marks/500) * 100
    print("percentage", percentage)

    if (percentage >= 80):
        print("Grade A")

    elif (percentage >= 60):
        print("Grade B")

    elif(percentage >= 50):
        print("Grade C")

    elif(percentage >= 40):
        print("Grade D")

    else:
        print("Failed")


