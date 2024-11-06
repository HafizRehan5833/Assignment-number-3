# Find the factorial of a number using a while loop.
num=int(input("enter the factorial number: "))
fact=1
count=num
while count > 0:
    fact*=count
    count-=1
print("The factorial of this number ",num,"is ",fact)
