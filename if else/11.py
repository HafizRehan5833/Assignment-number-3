#11. Check if a given number is a multiple of both 3 and 5.
user_input=int(input("Enter the number : "))

if user_input % 3 == 0 and user_input % 5 == 0:
    print(user_input," is mutiple of 3 and 5..")
else:
    print(user_input," is not a mutiple of 3 and 5..")