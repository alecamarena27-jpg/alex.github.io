#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Display Enter a number
#Display Enter a number
#If the numb1 is greater than numb2 make a subtraction and save the value on num3
#Display the results by the number order 
#If numb2 is greater than numb1 make a subtraction and save the value on num3
#Display the results by the number order 

import random


def main():
    show_large()
    
    
    
def show_large():
    numb1 = random.randint(1,5)
    numb2 = random.randint(1,5)
    
    if numb1 > numb2:
        numb3 = numb1 - numb2
        print(f"{numb1} is larger than {numb2} by {numb3}")
    elif numb2 > numb1:
        numb3 = numb2 - numb1
        print(f"{numb2} is larger than {numb1} by {numb3}")
    else:
        print(f"{numb1} is equal to {numb2} ")
        
        




if __name__ == "__main__":
    main()