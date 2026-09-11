#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Enter the first name and save it in First_name variable
#If the name is '' break the loop
#Enter the age and save it in Name_age variable
#Write Name and age variable in the friends.txt





while True: 
    
    
    First_name =input("Enter first name of friend or Enter to quit ")
    
    if First_name == '':
        break
    
    Name_age = int(input("Enter age (integer) of this friend "))
    
    with open("friends.txt", "a") as CAMARENA6PRE:
        CAMARENA6PRE.write(f" {First_name}\n")
        CAMARENA6PRE.write(f"  {Name_age}\n")




