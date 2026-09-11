#Program2_1.py
#By Alex Camarena, ID 2560886
# #COURSE NUMBER:0665
# Collaborator: none

#Pseudocode
#Display bar options
#Enter an option
#If the option is 1 enter the title of the game and retrieve the developer
#If the option is 2 add a new title and its developer
#If the option is 3 Enter the title of the game and get the new developer name and display the updated
#If the option is 4 Enter the title of the game and delete the title of the game and its developer
#If the option is 5 display all title from the Title dictionarie
#IF the option is 6 display all title and its developers from the Title dictionarie
#If the option is 7 display only the titles from the dictionarie
#If the option is 8 stop the program. 

Title = {}

print("-" * 70)
print()
print("Menu")

print("1. Look up a game by title")
print("2. Add a new title and its developers")
print("3. Change the existing developer(s) for a title")
print("4. Delete an existing title and its developers")
print("5. Print the number of titles")
print("6. Print all titles and developers")
print("7. Print all titles")
print("8. Quit")
print()


def choice_1():
    game = input("Enter the title of the game: ")

    if game in Title:
        print(f"The developer(s) of '{game}' is/are: {Title[game]}")
    else:
        print("title not found")

def choice_2():
    game = input("Enter the title of the game: ")
    developer = input("Enter the developer(s) of the game: ")
    Title[game] = developer

def choice_3():
    game = input("Enter the title of the game: ")

    if game in Title:
        new_developer = input("Enter the new developer(s) of the game:  ")
        Title[game] = new_developer
        print(f"The developer(s) for {game} has/have been updated.")
    else:
        print("title not found")

def choice_4():
    game = input("Enter the title of the game: ")
    
    if game in Title:
        del Title[game]
        print(f"The title {game} and its developer(s) have been deleted.")
    else:
        print("title not found")
        

def choice_5():
    print(f"The number of titles is: {len(Title)}")


def choice_6():
    for title_developers in Title.items():
        print(title_developers)
    
    
def choice_7():
    for game in Title:
        print(game)

def main():
    while True:
        choice = input("Enter your choice: ")

        if choice == "2":
            choice_2()
        elif choice == "1":
            choice_1()
        elif choice == "3":
            choice_3()
        elif choice == "4":
            choice_4()
        elif choice == "5":
            choice_5()
        elif choice == "6":
            choice_6()
        elif choice == "7":
            choice_7()
        elif choice == "8":
            print("Good Bye :)")
            break
        

main()
