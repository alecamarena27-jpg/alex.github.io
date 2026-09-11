#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none


#Pseudocode
#Display get the album name
#Display get the artis name
#Display get the price value
#Display get the discount
#Create a txt. doc in CAMARENA6
#Save album name in CAMARENA6
#Save artis name in CAMARENA6
#Save price value in CAMARENA6
#Save discount value in CAMARENA6
#Display The LP sale data has been successfully stored in lpsale.txt.
#Close CAMARENA6

artis = ''
price = ''
discount = ''
title = ''


while True:
        
        
    
    album = input("Enter the album's title: ")
    if album == '':
        print("he LP sale data has been successfully stored in lpsale.txt.")
        break
        
    
    artis = input("Enter the artist(s) name(s): ")
    if artis == '':
        print("he LP sale data has been successfully stored in lpsale.txt.")
        break
    
    price= input("Enter the regular price: ")
    if price == '':
        print("he LP sale data has been successfully stored in lpsale.txt.")
        break
    
    discount = input("Enter the discount in percent: ")
    if discount == '':
        print("he LP sale data has been successfully stored in lpsale.txt.")
        break
    with open("lpsale.txt", 'a') as CAMARENA6:
        CAMARENA6.write(album + '\n')
        CAMARENA6.write(artis + '\n')
        CAMARENA6.write(price + '\n')
        CAMARENA6.write(discount + '\n')
    
    print("The LP sale data has been successfully stored in lpsale.txt.")
CAMARENA6.close()





