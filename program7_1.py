import random

#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none


#Display the 8x8 square
#Generate the 8x8 with ramdon number from 0 to 200
#Get the sum of all age using the numbers in the square and save the resul in total
#Get the least number 
#Get the maximun number
#Get the average divided by total
#Called count function
#Get the seedlings by the stadistic requeriments
#Get the saplings by the stadistic requeriments
#Get the pole by the stadistic requeriments
#Get the mature by the stadistic requeriments
#Get the old_growth by the stadistic requeriments
#Display the results




def count(table):
    seedlings = 0
    saplings = 0
    pole = 0
    mature = 0
    old_growth = 0

    for row in table:
        for age in row:
            if 0 <= age <= 2:
                seedlings += 1
            elif 3 <= age <= 20:
                saplings += 1
            elif 21 <= age <= 50:
                pole += 1
            elif 51 <= age <= 100:
                mature += 1
            else: 
                old_growth += 1

    print("Number of seedlings:             ", seedlings)
    print("Number of sapling-aged trees:    ", saplings)
    print("Number of pole stage-aged trees: ", pole)
    print("Number of mature-aged trees:     ", mature)
    print("Number of old growth-aged trees: ", old_growth)




def main():
    
    table = []
    total = 0
    oldest = 0
    youngest = 0
    
    for row in range(8):
        new_table = []
        
        for column in range(8):
            new_table.append(random.randint(0, 200))
            
        new_table.sort(reverse=True)
        table.append(new_table)
        
    
    print()
    for row in table:
        youngest = row[0]
        
        for num in row:
            if num < youngest:
                youngest = num
            
            print(f"{num:4}", end="")
            total += num
            
            if num > oldest:
                oldest = num
            
 
        
        print()
    print()
    
    print("Sum of all ages: ",total)
    print(f"Oldest age:", oldest)
    print(f"Youngest age:", youngest)
    
    average = total / 64
    print(f"Average age: {average:.2f}")
    
    print()
    count(table)
    
    
main()