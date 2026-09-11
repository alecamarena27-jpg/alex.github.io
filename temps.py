#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Calculate the F value base on the formula
#Calculate the C value base on the formula




def f_to_c(f):
    
    constant = 32
    constant2 = 1.8
    Celsius = f - constant
    Result = Celsius / constant2
    return Result
    
def c_to_f(c):
    constant = 32
    constant2 = 1.8
    Fahrenheit = c * constant2
    fah = Fahrenheit + constant
    
    
    
    print( f"{c}Celsius is {fah:.1f}Fahrenheit")