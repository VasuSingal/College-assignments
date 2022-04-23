SID = input("Enter SID:")
name = input("Enter Name:")
gender = input("Enter Gender (F: female)(M: male)(U: unknown):")
course_name = input("Enter the Course Name:")
CGPA = input("Enter the CGPA(to 1 decimal place):")

Student = list[SID, name, gender, course_name, CGPA]

print(Student)