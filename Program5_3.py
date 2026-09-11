import program5_2
#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Import module_2
#Display enter the length
#Display enter the width
#Display enter the height
#Import function surface
#Import function sqrt
#Import function volume
#Display the surface result
#Display the sqrt result
#Display the volume result
def main():
    
    length = float(input("Enter the length of the rectangular cuboid: "))
    width = float(input("Enter the width of the rectangular cuboid: "))
    height = float(input("Enter the height of the rectangular cuboid: "))
    
    program5_2.surface(length, width, height)
    program5_2.sqrt(length, width, height)
    program5_2.volume(length, width, height)
    


if __name__ == "__main__":
    main()

