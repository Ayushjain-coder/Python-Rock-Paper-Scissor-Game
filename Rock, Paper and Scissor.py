# Rock, Paper and Scissor Game
import random as rdm

game_choice = {'Rock':1,'Paper':2,'Scissor':3}

print("Welcome to Rock, Paper and Scissor Game")

rules = {'Rock vs Paper':'Paper', 'Paper vs Scissor':'Scissor', 'Scissor vs Rock':'Rock'}

print("Rules For This Game:")

i=1

for key, value in rules.items():
    print(str(i) + "). " + key + "  --Win-->  " + value)
    i += 1

print()
print("Select Your Choice:")
print("1. Rock" + " " + "2. Paper" + " " + "3. Scissor")

check = 'Y'

while check == 'Y' or check == 'y':
    print()
    user_choice = int(input("Its Your Turn: "))

    if (user_choice <= 3) and (user_choice >= 0):
        if user_choice == 1:
            print("Your Choice: Rock")
        elif user_choice == 2:
            print("Your Choice: Paper")
        else:
            print("Your Choice: Scissor")
    else:
        print("Please Enter The Choice Between 1 to 3")
        user_choice = int(input("Its Your Turn: "))

    print()
    print("Now Its Computer Turn")
    computer_choice = rdm.choice(['Rock','Paper','Scissor'])
    print("Computer Choice: "+ computer_choice)

    for key, value in game_choice.items():
        if user_choice == value:
            user_choice = key

    if user_choice == computer_choice:
        check = 'Y'
    else:
        print()
        for keys in rules.keys():
            key = keys.split(" vs ")
            if (user_choice in key) and (computer_choice in key):
                if computer_choice == rules[keys]:
                    print(computer_choice + " wins: " + "Computer is Winner!!!")
                if user_choice == rules[keys]:
                    print(user_choice + " wins: " + "You are Winner!!!")

        print()
        check = input("Do You Want To Play Again(Y/N): ")
else:
     print("Thanks For Playing With Us.....")            
