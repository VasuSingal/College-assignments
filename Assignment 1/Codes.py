#Question 1
a = input("Enter the numbers in the format(x y z):")

x = list(map(int, a.split()))

print ("Average of the three numbers is= ", (x[0] + x[1] + x[2])/3)

#-------------------------------------------------------------------------------------------------------

#Question 2
Gross_Income = int(input("Enter the Gross Income :"))
dependents = int(input("Enter the number of Dependents :"))

taxable_income = Gross_Income-10000 - (3000*dependents)

tax = taxable_income*0.2

print("Tax to be paid = ", tax)

#------------------------------------------------------------------------------------------------------

#Question 3
SID = input("Enter SID:")
name = input("Enter Name:")
gender = input("Enter Gender (F: female)(M: male)(U: unknown):")
course_name = input("Enter the Course Name:")
CGPA = input("Enter the CGPA(to 1 decimal place):")

Student = list[SID, name, gender, course_name, CGPA]

print(Student)

#------------------------------------------------------------------------------------------------------

#Question 4
marks_input = input("Enter the marks of 5 students separated by a space :")

marks = list(map(int, marks_input.split(" ")))
marks.sort()

print(marks)

#------------------------------------------------------------------------------------------------------

#Question 5
COLOUR_LIST=["Red","Green","White","Black","Pink","Yellow"]    #original list
print(COLOUR_LIST)

del COLOUR_LIST[3]
print(COLOUR_LIST)      #list obtained after deleting colour black

COLOUR_LIST[3]="Purple"
print(COLOUR_LIST)       #list obtained after replacing 4th and 5th element with pink colour
