#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Display the different types of shoelaces
#Repeat the loop base on the types of shoelaces
#Display the number of eyelet pairs
#Display enter the quantity
#Calculate the quantity and eyelet
#Display the subtotal
#Calculate the total
#Display the total

counter = 0

from module import mult_ti, total_amount

def main():
    total = 0
    
    showlaces = int(input("Enter the number of different types of shoelaces being purchased:"))
        
    for counter in range(showlaces):
        
        
        print(f"item", counter + 1 )
        
        eyelet = int(input("Enter the number of eyelet pairs: "))
        quantity = int(input("Enter the quantity: "))
        
        subtotal = mult_ti(eyelet, quantity)
        print(f"subtotal for item: ${subtotal:.2f}")
        
        total = total_amount(total, subtotal)
    print()
    print(f"Total: ${total:.2f} ")

if __name__ == "__main__":
    main()



