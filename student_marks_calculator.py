name = input("Enter your name: ")

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("Student:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", percentage, "%")

if m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("Result: Pass")
else:
    print("Result: Fail")
