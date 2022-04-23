a = input("Enter the numbers in the format(x y z):")

x = list(map(int, a.split()))

print ("Average of the three numbers is= ", (x[0] + x[1] + x[2])/3)
