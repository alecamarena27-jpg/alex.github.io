#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Display Enter an interger or 0 to quit
#Calculate if the value is equal 0 end the program
#Calculate is the result of the integer divide by 2 remain in 1 display odd number
#Display even number if the value remain is 0

while True :
    number = int(input("Enter an integer or 0 to quit: "))
    
    if number == 0:
        print("All done")
        break  
        
    if number % 2 == 1:
        print(f"{number} is an odd number")
    else:
        print(f"{number} is an even number")


