# Snake Water Gun Game in  Python :)
import random

print("Welcome To Snake Water Gun Game")
print("Hope You Know The Rules ..!!")
print("Here,\n\tTo choose Snake press : 's' ")
print("\tTo Choose Water press : 'w' ")
print("\tTo Choose Gun press : 'g' ")
Uscore = 0 # for storing User's Score
Cscore = 0 # for storing Comp's Score
chance = int(input("How Many Times You Want to play: ")) #Basically Turns
a = 1 #This Variable will Count No. of Games or serve as a Index
while (chance != 0):
    print("Game No: ", a)
    a = a+1
    chance = chance-1
    turn = (input("Enter Your Choice: "))

    user=0 #This will show that game is not started yet!
    if (turn == 's'):
        user = 1
    elif (turn == 'w'):
        user = 2
    elif (turn == 'g'):
        user = 3
    else:
        print('Wrong input..!!')
        break

    if (user == 1):
        print("You Have Choosen Snake..!🐍")
    elif (user == 2):
        print('You Have Choosen Water..!🐳')
    elif (user == 3):
        print('You Have Choosen Gun..!🔫')

    # Generating Random no for computer turn

    comp = random.randint(1, 100) % 3+1 #generating random no.s for Comp

    if (comp == 1):
        print("Comp Have Choosen Snake..!🐍")
    elif (comp == 2):
        print('Comp Have Choosen Water..!🐳')
    elif (comp == 3):
        print('Comp Have Choosen Gun..!🔫')

    if (user == comp):
        print("Its a Tie..!!")
    elif (user == 1 and comp == 2):  # user=snake and comp=water
        print("You Win>>!!")
        Uscore = Uscore+1
    elif (user == 1 and comp == 3):  # user=snake and comp=Gun
        print("Comp Win>>!")
        Cscore = Cscore+1
    elif (user == 2 and comp == 1):  # user=water and comp=snake
        print("Comp Wins>>1")
        Cscore = Cscore+1
    elif (user == 2 and comp == 3):  # user=water and comp=gun
        print("You Wins>>!")
        Uscore = Uscore+1
    elif (user == 3 and comp == 1):  # user=Gun and comp=snake
        print("You Wins>>!")
        Uscore = Uscore+1
    elif (user == 3 and comp == 2):  # user=gun and comp=water
        print("Comp Wins>>!")
        Cscore = Cscore+1

print("\tYou Have Scored: ", Uscore) #This will display scores for User
print("\tComp Scored: ", Cscore) #This will display scores for Comp
