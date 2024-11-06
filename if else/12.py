#12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
temp=float(input("Enter the temperature in celcius: "))
if temp >= 0 and temp <=30:
    print("Your temperature is freezing.")
elif temp > 35 and temp <=37  :
    
    print("Your temperature is moderate.")
else:
    print("Your Temperature is hot")    
