#11. Print the reverse of a given number.

# Get user input
number = int(input("Enter an integer: "))

# Initialize reversed number to zero
reversed_number = 0

# Use a loop to reverse the digits
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Shift digits and add last digit
    number = number // 10  # Remove the last digit

print("The reversed number is:", reversed_number)
