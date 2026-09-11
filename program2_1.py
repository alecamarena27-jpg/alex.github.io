#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#PSEUDOCODE
#prompt user for meal, assign a value to meal
#prompt user for tip, assign a value to tip
#dived tip / 100
#multiply meal by avg1
#multiply meal by TAX
#Add the avg, tax_amount and meal
#print the results of meal, tip, avg, tax_amount and total

TAX = 0.07
meal = float(input("What is the total cost of the meal?"))
tip = int(input("What is the tip percentage?"))

avg1 = tip / 100

avg = meal * avg1

tax_amount = meal * TAX

total = avg + tax_amount + meal

print(f"A ${meal:.2f} meal with a {tip:.0f}% tip of ${avg:.2f} and 7% tax which is {tax_amount:.2f}$ has a grand total cost of {total:.2f} ")
