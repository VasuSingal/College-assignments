marks_input = input("Enter the marks of 5 students separated by a space :")

marks = list(map(int, marks_input.split(" ")))
marks.sort()

print(marks)