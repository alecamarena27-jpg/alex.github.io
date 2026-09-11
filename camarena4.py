#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudo code
#Display the table header. INIT, SQUARES, CUBES
#Calculate the square of the number on range
#Calculate the cube of the number on range
#Display the Range value in INIT column
#Display the squares values in SQUARES column
#Display the cubes values in CUBES column
#Display the INIT, SQUARES, CUBES in a table column format

print('+-------+--------+------------+')
print(f'|{"INIT":^7}|{"SQUARES":^8}|{"CUBES":^12}|')
print('+-------+--------+------------+')


for x in (range(5, 51, 5)):
    square = x ** 2
    cube = x ** 3
    print(f'|{x:^7}|{square:>8,.0f}|{cube:>12,.0f}|')
    print('+-------+--------+------------+')