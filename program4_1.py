#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Display Enter the start for US tons. If the value is less o equal 0, display the value can not be negative or zero,if don`t. Print the start value
#Display Enter the stop for US tons. If the value is less o equal 0, display the value can not be negative or zero,if don`t. Print the stop value
#Display Enter the stop for US tons. If the value is less o equal 0, display the value can not be negative or zero,if don`t print the stop value
#Calculate the values enter by us and make a range from value_1 to value_2 and make steps with value_3
#Convert US_TONS to Imperial tons by multiply us times IMPERIAL_TONS
#Display in a chart the US tons and Imperial Tons


IMPERIAL_TONS = 0.892857143


while (start := int(input("Enter the start for US tons: "))) <= 0:
    print("Start value for US tons cannot be negative or zero")
else:
    print(f"Enter the start for US tons {start}")


while (stop := int(input("Enter the stop for US tons: "))) <= 0:
    print("Stop value for US tons cannot be negative or zero")
else:
    print(f"Enter the stop for US tons {stop}")



while (step := int(input("Enter the step for US tons: "))) <= 0:
    print("Step value for US tons cannot be negative or zero")
else:
    print(f"Enter the stop for US tons {step}")



print(f'  {"US TONS":^7}    {"IMPERIAL TONS":^8}')
for us in range (valor := start, valor_2 := stop + 1, valor_3 := step):
    US_TONS =  us * IMPERIAL_TONS
    print(f"{us:^10}   {US_TONS:>13.3f}")


