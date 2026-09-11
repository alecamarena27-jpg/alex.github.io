#Program2_2.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

# PSEUDOCODE
# Prompt the user for the number of hours
# Store the value in the variable hours
# Convert hours to days by dividing hours by 24
# Store the result in X
# Calculate the remaining hours using for Y
# Store the result in Y
# Display the number of days
# Display the remaining hours

X = int(input("What is the number of hours to convert to days and hours?"))

Y = X // 24

Z = X % 24

print(f"{X} hours is equivalent to {Y} day and {Z} hours")
