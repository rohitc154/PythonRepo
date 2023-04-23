'''
    S W G
    0 1 2
S 0 D W L
W 1 L D W
G 2 W L D
'''
from random import *
from string import *

l1 = ["snake","water","gun"]
cval = choice(l1)

uval = input("Enter your choice(Snake/water/gun) : ")
luval = uval.lower()

# print(luval)

if cval == luval:
    print("Choices Tie")

elif cval == "snake" and luval == "water":
    print("Computer Win!")
    
elif luval == "snake" and cval == "water":
    print("You Win!")

elif cval == "snake" and luval == "gun":
    print("You Win!")

elif luval == "snake" and cval == "gun":
    print("Computer Win!")

elif cval == "water" and luval == "gun":
    print("Computer Win!")

elif luval == "water" and cval == "gun":
    print("You Win!")
else:
    print("Enter valid input!")