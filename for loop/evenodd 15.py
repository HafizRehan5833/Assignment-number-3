#. Print the sum of even and odd numbers separately up to a given number
num=int(input("Enter the number:"))
a=input("Which  numbers you want to sum (Please enter even or odd) : ")
a=a.lower()
even=0
odd=0

for i in range(1,num+1):
    if i%2==0:
        even+=i
    else:

        odd +=i 
if a=="even":        
    print("Your number is even.Sum of all numbers: ",even)
else:
    print("Your number is odd.Sum of all numbers:",odd)           
