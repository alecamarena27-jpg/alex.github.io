#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudocode
#Display to the user the follow caracter Album Title, Artist(s), Name(s), Discount ($), Total price after discount  ($)
#Open the lpsale.txt and display to read the content
#Get into CAMARENA6 Folder read and retrieve the albums value
#Get into CAMARENA6 Folder read and retrieve the artis value
#Get into CAMARENA6 Folder read and retrieve the price value
#Get into CAMARENA6 Folder read and retrieve the discount value
#Get the total_price 
#Display the album, artis, discount, and total_price





with open("lpsale.txt", 'r') as CAMARENA6:
    print ()
    print("Album Title                            Artist(s)   Name(s)              Discount ($)      Total price after discount  ($)")
    print()
    print("-------------------------------------------------------------------------------------------------------------------------")
    print()
    
    
    albums = CAMARENA6.readline().strip()
    
    while albums != "":
        artis = CAMARENA6.readline().strip()
        price = CAMARENA6.readline().strip()
        discount = CAMARENA6.readline().strip()
        
        total_price = float(price) - (float(price) * float(discount) / 100)
        
        print(f"{albums:<40}{artis:<35}{float(discount):<25.2f}{float(total_price):<20.2f}" )
        print()
        albums = CAMARENA6.readline().strip()
