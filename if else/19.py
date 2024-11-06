#19. Check if a string input is uppercase, lowercase, or a mix.

string=input("Enter the string: ")

if string.isupper():
    print(string,"is Uppercase.")
elif string.islower():
    print(string,"is lowercase.")

else:
    print(string,"is mix.")        