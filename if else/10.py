#10. Write a program to determine if a given character is a vowel or consonant.
user_input=input("Enter input value: ")
small=user_input.lower()

vowels=["a","e","i","o","u"]

if small in vowels:
    print(small," is vowel." )
else:
    print(small," is  consonants.")    