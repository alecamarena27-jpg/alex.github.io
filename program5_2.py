import math

#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Display enter the length
#Display enter the width
#Display enter the height
#Calculate the surface
#Calculate the diagonal
#Display the volume
#Display the length
#Display the surfaces
#Display the Diagonal


def main():
    
    length = float(input("Enter the length of the rectangular cuboid: "))
    
    width = float(input("Enter the width of the rectangular cuboid: "))
    
    height = float(input("Enter the height of the rectangular cuboid: "))
    
    surface(length, width, height)
    
    
    sqrt(length, width, height)
    
    
    volume(length, width, height)
    
    

def volume(length, width, height):
    volumen = length * width * height
    print(f"The volume of the rectangular cuboid is: {volumen:.3f}")


def sqrt(length, width, height):
    diagonal = math.sqrt(length**2 + width**2 + height**2)
    print(f"The diagonal of the rectangular cuboid is {diagonal:.3f}")



def surface(length, width, height):
    surface = (length * width) * 2
    surface_2 = (length * height) * 2
    surface_3 = (width * height) * 2
    surface_4 = surface + surface_2 + surface_3
    print(f"The surface area of the rectangular cuboid is {surface_4:.4f} ")









if __name__ == "__main__":
    main()
    
    