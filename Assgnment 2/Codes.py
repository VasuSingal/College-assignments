# Question 1
main_string = "Python is a case sensitive language"

print(len(main_string))                                              #A

print(main_string[::-1])                                             #B

print(main_string[10:26])                                            #C

print(main_string.replace("a case sensitive", "object oriented"))    #D

c=0                                                                  #E
for c in range(len(main_string)):
    if main_string[c]=="a":
        print(c)
        c+=1
    else:
        c+=1                                         

print(main_string.replace(" ",""))                                   #F

#------------------------------------------------------------------------------------------------------------------------------------

# Question 2
my_name = "Vasu Singal"
SID = 21102035
department_name = "Civil Engineering"
CGPA = 8.56

print("Hey,",my_name,"Here!\nMy SID is",SID,"\nI am from",department_name,"department and my CGPA is",CGPA)

#------------------------------------------------------------------------------------------------------------------------------------

# Question 3
a = 56 
b = 10

print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)

#------------------------------------------------------------------------------------------------------------------------------------

# Question 4
a = input("Enter the string:")

x = a.find("name")

if x==-1:
    print("No")
else:
    print("Yes")

#------------------------------------------------------------------------------------------------------------------------------------

# Question 5
a = int(input("Enter the length of side 1:"))
b = int(input("Enter the length of side 2:"))
c = int(input("Enter the length of side 3:"))

while (a+b>c and b+c>a and c+a>b):
    print("Yes")
    break
while (a+b<=c or b+c<=a or c+a<=b):
    print("No")
    break
    
#------------------------------------------------------------------------------------------------------------------------------------
    
# Question 6
flips = 0
a = int(input("Enter the number = "))
b = int(input("Enter the number = "))

for x in range(a+b):
    t1 = a&1
    t2 = b&1
    if (t1 != t2):
        flips+=1

    a>>=1
    b>>=1

print(flips)
