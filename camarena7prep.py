#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none


#Display the name variable values
#Display the 4 Element in the list
#Display the 9 Element in the list
#Display the smallest element
#Display the size of the list
#Display the new size list



import random

def main():
    
    list = []
    
    print()
    for i in range(12):
        list.sort()
        list.append(random.randint(50, 100))
        
    for name in list:
        
        print(name, end=" ")
        
    print()
    change_list(list)
    print
    size(list)
    

def change_list(list):
    
    print("The 4th element in the list is", list[3])
    print("The element at index 9 is", list[9])
    print("The smallest element in the list is", (min(list)))
    

def size(list):
    
    middle = list[3:9]
    
    middle.sort()
    
    print(f"The size of the list is now {len(middle)}")
    print(*middle)
    return middle
    
    
    
    

main()
print()