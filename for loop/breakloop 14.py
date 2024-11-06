#Write a program that breaks the loop when a certain condition is met.


a=int(input("Enter the minimum number: "))
c=int(input("Enter maximum number  (loop run) : "))
b=int(input("Enter break value : " ))
while a<=c:
    if a == b:
        print("In", a," point Loop end")
        break
    print(a)
    a+=1