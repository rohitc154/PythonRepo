'''One option is randomly generated by computer and one by the user:
Winning Rule :
Rock vs Paper = Paper Wins
Paper vs Scissor = Scissor Wins
Rock vs Scissor = Rock Wins
'''

import random

l1 = ("Rock","paper","Scissor")
x = random.choice(l1)
l1val = x.lower()

countc = 0
countu = 0
i = 0
while i<5:
    user = input("Enter Your Choice(Rock/Paper/Scissor) : ")
    userval = user.lower()

    if userval == 'rock' and l1val == 'paper':
        print("Computer Wins!")
        countc += 1
    elif l1val == 'rock' and userval == 'paper':
        print("you Win!")
        countu += 1
    elif userval == 'paper' and l1val == 'scissor':
        print("Computer Wins!")
        countc += 1
    elif userval == 'scissor' and l1val == 'paper':
        print("you Win!")
        countu += 1
    elif userval == 'rock' and l1val == 'scissor':
        print("You Win!")
        countu += 1
    elif userval == 'scissor' and l1val == 'rock':
        print("Computer Wins!")
        countc += 1
    elif userval == l1val:
        print("Choosed tie!")
    else:
        print("Enter Correct Choice !")
    i+=1

print("\nComputer's Score : ",countc,"Your Score : ",countu)

if countu < countc:
    print("Computer's Wins overall Match!")
elif countc < countu:
    print("You Win overall Match!")
elif countc == countu:
    print("Match tie!")
