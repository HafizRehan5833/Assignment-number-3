#. Print all prime numbers between 1 and 50.
num=int(input("Enter number: "))

while num <=50:
    if num %2 != 0 and num % 3 != 0 and num % 5 != 0:
        print(num)
    else:
        pass

    num+=1

