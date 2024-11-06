number=int(input("Enter the number: "))


if number%2 != 0 and number%3 != 0 and number%5 != 0:
    print(number," is primenumber")
else:
    print(number," is not primenumber")