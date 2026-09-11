#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Open the CAMARENA6PRE file
#Read the CAMARENA6PRE until get 0 string
#Save the first string in the variable name
#Save the second string and son on in the variable age
#Display name and age for each two string
#Plus 1 in the variable counter for each time the loop ends
#Plus the age variable number with accumulator variable
#Performace a division between accumulator and counter and save the result in Average variable
#Display Average



counter = 0
accumulator = 0

with open("friends.txt", "r") as CAMARENA6PRE:
    while True:
        name = CAMARENA6PRE.readline().strip()
        if not name:
            break
        
        age = int(CAMARENA6PRE.readline().strip())
        
        print(f"My friend {name} is {age}")
        
        accumulator += age
        counter += 1
        Average = accumulator / counter
        
        
print(f"Average age of friends is {Average:.0f}")


