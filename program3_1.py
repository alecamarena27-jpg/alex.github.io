#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none


# Pseudo code
# Display How many guitar picks do you wish to buy?
# Apply a different price if the number of picks reach 1 dozen
# Apply a different price if the number of picks reach 2 dozen
# Apply a different price if the number of picks reach 3 dozen
# Calculate the total price by multiply pick_numbers by price
# Display the total price to pay


Picks_numbers = int(input("How many guitar picks do you wish to buy?: "))


if Picks_numbers >= 36:
     Price = 0.19
     
elif Picks_numbers >= 24:
    Price = 0.21
    
elif Picks_numbers >= 12:
    Price = 0.23
    
else: 
    
    Price = 0.25
    


total = Picks_numbers * Price



print (f"Total cost of guitar picks is ${total:.2f}")
