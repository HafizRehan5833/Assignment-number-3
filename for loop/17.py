#. Write a program that continues to ask for a number until the correct number is guessed.

import random
random.randint()


num=input("Enter the guess:")

while True:
    if num=="q":
        break
    elif num == num :
        print(num,"is the guess")
    else:
        print("Try again")    
    