#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none


def mult_ti(eyelet, quantity):
    while True:
        if eyelet != 0:
            subtotal = (eyelet * quantity) * 0.50
            
            return subtotal
        else:
            print("Purchase canceled")
            
def total_amount(total, subtotal):
    return total + subtotal
    
