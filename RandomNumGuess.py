# Computer guessed a random number, and you have to show that your guessed number is greater, lesser or equal to the computer guessed
# number.

from random import *

x = randint(1,20)

while True:
    try:
        num = int(input("Guess a number (between 1 and 20) : "))
        if num > x:
            print("You guessed a Greater number")
        elif num < x:
            print("You guessed a Smaller number")
        elif(num == x):
            # out = "Congratulation!{a} {b} you guessed the correct number."
            # print(out.format(a = chr(9825),b = chr(9734)))
            a = chr(9825)
            b = chr(9734)
            print(f"Congratulation! {a} {b} you guessed the correct number.")
            break
        elif(num == 0):
            break
        
    except:
        print("Enter Integer value. Invalid Input!")

