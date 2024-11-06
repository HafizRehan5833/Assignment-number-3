#2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.
age=int(input("Enter Your age quit for q : "))


if age <= 1:
    print("You in infant age.")
elif age >=1 and age <= 4 :
    print("You in Toddler age.") 
elif age > 4 and age <= 12:
    print("You in child age.")
elif age > 12  and age <= 18:
    print("You in Adult Teen age.")
elif age > 18 and age <= 40:
    print("You in adult middle age.")
elif age > 40 and age <= 60:
    print("You in adult age.")
else:
    print("You in senior citizen age." )

