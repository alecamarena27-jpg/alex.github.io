#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudocode
#Display Enter state abbrev. or Enter to quit:
#Display "is already in the dictionary" if the state is the same as in states variable if not
#Get the capital
#Display the number of elements in the dictionarie
#Retrieve all elements in the states dictionarie
#Display all states in the states dictionarie.



states = { 'FL':'Tallahasee', 'VA':'Richmond', 'NJ':'Trenton', 'RI':'Providence'}
print("4 states are in the dictionary \n Let's add a few more: " )

while True:
    
    abbrev = input("Enter state abbrev. or Enter to quit: ")
    
    if abbrev == "":
        break
    
    if abbrev in states:
        print(f"{abbrev} is already in the dictionary.")
    else:
        capital = input(f"Enter the capital of {abbrev}: ")
        states[abbrev] = capital
        
print()
print(f"Got {len(states)} states now. Here they are...")
print()


for total_states_capital in states.items():
    print(total_states_capital)
    

print()

#Pseudocode
#Write the number list in the total variable
#Calculate the cube of all numbers in total variable
#Write the total cube numbers in cubed variable
#Print all cubed results

def cubed_1():
    Number = [1,3,5,7,9]
    cubed  = {}
    
    for total in Number:
        cubed [total] = total**3
    
    for Number in cubed:
        print(  f"{Number} cubed is {cubed[Number]}"  )
    
    
cubed_1()