#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none


#Pseudo code
#Display the outter variable row 4 times
#Display the argument in print
#Display the inner variable column 8 times
#Display print argument 8 times



for row in range(5):
    print("0123456789")
    
    
    for column in range(8): 
        print("0        9",)
        
    
    print("0123456789")
    print()



import random

def main():
    
    table = []
    
    for row in range(8):
        new_table = []
        
        for column in range(8):
            new_table.append(random.randint(0, 200))
            
        new_table.sort()
        table.append(new_table)
        
    for row in table:
        print(f"--{row}--")


main()
