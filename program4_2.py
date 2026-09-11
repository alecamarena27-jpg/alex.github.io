#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code.
#Display enter the FSA value less than 3200
#Display enter the expense value  
#Get the expense value and save it in total_expenses
#Add the expense values as many times posible
#Make a count of how many time the user put a expense value
#Display the times that user inser an expense value
#Display the accumulated of FSA
#Calcula if the total_expenses is greater than FSA subtrack total_expenses - FSA
#Calculate if the total_expenses is lees than FSA subtrack FSA less totla_expenses
#If the FSA and the total_expenses is equal to FSA display that total_expenses is equal to FSA


total_expenses = 0
FSA_1 = 0

while (FSA := int(input("Enter your FSA contribution for the year as a whole number (max allowed is 3200):"))) <= 3200:
    
    while (expense := int(input("Enter the FSA expenditure as a whole number (enter 0 to finish): "))) != 0:
        total_expenses += expense
        FSA_1 += 1 
    
    print(f"You have a count of {FSA_1} FSA expenditures for the year.")
    print(f"You have accumulated a total of {total_expenses} for the year.")
    
    
    if total_expenses > FSA:
        diferential = total_expenses - FSA
        print(f"Your expenditure total is ${diferential} over your FSA contribution for the year.")
    elif total_expenses < FSA:
        diferential = FSA - total_expenses
        print(f"Your expenditure total is ${diferential} under your FSA contribution for the year.")
    else:
        print("Your expenditure total is the same as your FSA contribution.")
        

        
    break