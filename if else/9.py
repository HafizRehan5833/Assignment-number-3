#Take three sides of a triangle as input and check if they form a valid triangle.
num1=float(input("Enter first side:"))
num2=float(input("Enter second side:"))
num3=float(input("Enter third side:"))


if  num1+num2>num3 and num1+num3>num2 and num2+num3>num1:
    print("Perfect triangle")
else:
    print("Invalid triangle..") 
       