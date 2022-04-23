from telnetlib import GA


Gross_Income = int(input("Enter the Gross Income :"))
dependents = int(input("Enter the number of Dependents :"))

taxable_income = Gross_Income-10000 - (3000*dependents)

tax = taxable_income*0.2

print("Tax to be paid = ", tax)