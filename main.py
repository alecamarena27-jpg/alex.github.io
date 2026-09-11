#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Display enter a temp value
#Display confir if was Fah or Cel
#If the range is f call the f_to_c function if don`t calle the c_to_f function`
#Display the result of the convertion

import temps

def main():
    
    temp = int(input("Enter a temperature "))
    range = input("Was that input Fahrenheit or Celsius c/f? ")
    
    
    if range == "f":
        
        c = temps.f_to_c(temp)
        
        print(f"{temp} Fahrenheit equals {c:.1f} Celsius")
        
    else:
        temps.c_to_f(temp)

if __name__ == "__main__":
    main()