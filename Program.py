#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#PSEUDO CODE
#Enter the amount of pounds
#Multiply the cost of cofe by the cofe pound
#Multiply the pound by the shipping
#Multipligly the cost of cofe by the 7%
#Display cost of cofe
#Display tax total
#Display shipping price if the price is over 150$ Display shipping free
#Display the add of cost of coffee, sales tax, shipping fee in total payable


tax = 0.07
delivery = 1

pound = int(input("How many pounds are you ordering?: "))

if pound >= 40:
    Pounds_price = 7.50

elif pound >= 20:
    Pounds_price = 8.75

elif pound >= 10:
    Pounds_price = 10.00

elif pound >= 1 and pound <= 9:
    Pounds_price = 12.00
    
else:
     Pounds_price = 0
     pound = 0
    

cost_of_coffee = pound * Pounds_price

if cost_of_coffee > 150:
    shipping = 0
else:
    shipping = delivery * pound

tax_pay = cost_of_coffee * tax

total = cost_of_coffee + shipping + tax_pay

print(f"Cost of coffee: ${cost_of_coffee:.2f}")
print(f"7% sales tax: ${tax_pay:.2f}")
print(f"Shipping fee: ${shipping:.2f}")
print(f"Total payable: ${total:.2f}")
