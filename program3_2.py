#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none


#Pseudo code
# Display enter three blood sugar levels
# Compare between blood_1, blood_2 and blood_ 3 and take the highest one and save it on the variable highest if don`t passed to the next block
# compare between blood_2 and blood_3 and take the highest one and save it on the variable hightes
# Get the total by adding blood_1, blood_2 and blood_3
# Get the average by subtracting the total from the highest one  
# Display the blood_sugar_level after dividing the average over 2

blood_1 = int(input("Enter first fasting blood sugar reading in mg/dL: "))
blood_2 = int(input("Enter second fasting blood sugar reading in mg/dL: "))
blood_3 = int(input("Enter third fasting blood sugar reading in mg/dL: "))



if blood_1 > blood_2:
    if blood_1 > blood_3:
        highest = blood_1
    else:
        highest = blood_3


else:
        if blood_2 > blood_3:
                highest = blood_2
        else:
                highest = blood_3
        
        
total = blood_1 + blood_2 + blood_3
average = total - highest

print("The average blood sugar for the patient is",blood_sugar_level := average / 2,"mg/dL")