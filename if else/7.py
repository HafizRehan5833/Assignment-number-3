#7. Write a program to find the largest of three numbers.

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))


if num1 > num2 and num1 > num3:
    print("Number1 is greater.")
elif num2 > num1 and num2 > num3:
    print("Number2 is greater.")    
elif num3 > num2 and num3 > num1:
    print("Number3 is greater.") 
else:
    print("Your number is same.Do not greater than each other.")       