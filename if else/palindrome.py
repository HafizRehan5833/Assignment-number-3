user_inpt=input("Enter your string :")

palindrome=user_inpt[::-1]
#print(palindrome)

if user_inpt == palindrome:
    print("Your string is palindrme.")
else:
    print("Your string is not palindrome.")     

#days=['Monday','Tuesday','Wednesday','Thursday','Friday']
#days.reverse()

#print(days)