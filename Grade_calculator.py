# SPC ID# 2560886 
# Alex Camarena
# #COURSE NUMBER:0665
# Collaborator: none


# Display Enter the score for test 1 #This one will ask the user to insert a value to the variable score1
# Convert score1 to float # Here the machine will convert the value inserted to a float number

# Display Enter the score for test 2 #This one will ask the user to insert a value to the variable score2
# Convert score2 to float # Here the machine will convert the value inserted to a float number

# Display Enter the score for test 3 #This one will ask the user to insert a value to the variable score3
# Convert score3 to float # Here the machine will convert the value inserted to a float number

# Set the "total" = score1 + score2 + score3 # Here it will add all the values collected

# Set the "average" = total divided by 3 # Here the code will divide the variable "total" by 3

# Display the average of these scores is #Here will show the prompt

# Display average #Here will this display the average result


score1 = float(input("Enter the score for test 1")) #This one will ask the user to insert a value to the variable score1 and also convert the number to float
score2 = float(input("Enter the score for test 2")) #This one will ask the user to insert a value to the variable score2 and also convert the number to float
score3 = float(input("Enter the score for test 3")) #This one will ask the user to insert a value to the variable score3 and also convert the number to float


total = score1 + score2 + score3  #Here the code will add all the values collected

average = total / 3 #Here it will divide the total variable by 3

print (f"The average of these scores {average:<.2f}%") #Here it will show the resul of the operation