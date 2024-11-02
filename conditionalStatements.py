mark = int(input("Enter your exam marks: "))

if (mark >100 or mark < 0):
    print("Input valid marks.")
elif(mark >= 80):
    print("Result is: A+")
elif(mark >= 60):
    print("Result is: A")
else:
    print("Fail")
