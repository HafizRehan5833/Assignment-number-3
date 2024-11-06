#16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).



# Function to classify the triangle
def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Input lengths of the sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the input forms a valid triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    # Classify the triangle
    triangle_type = classify_triangle(side1, side2, side3)
    print(f"The triangle is {triangle_type}.")
else:
    print("The entered values do not form a valid triangle.")

