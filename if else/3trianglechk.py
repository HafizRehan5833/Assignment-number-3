side1=int(input("Enter fisrt side: "))
side2=int(input("Enter second side: "))
side3=int(input("Enter third side: "))


if side1 == side2 == side3 :
    print("Your triangle is equilateral.")
elif (side1 == side2) != side3:
    print("Isoceles") 