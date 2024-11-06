# Write a program to print the first 10 Fibonacci numbers.

a= int(input("Enter first number: "))
b=int(input("Enter second number: "))

#print("The first 10 Fibonacci numbers are:")

for i in range(10):
    print(a)
    a, b = b, a + b
