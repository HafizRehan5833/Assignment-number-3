#17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

num=int(input("Enter the number: ")) 

if num%2 == 0 or num%3 == 0:
    print(num,"is 2 divisible.")

else:
    print(num,"is not divisible by 2 and 3.")    