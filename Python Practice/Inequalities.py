# Receive age and store in age and convert to integer with "evel"
age = eval(input("Enter age: "))
# If age is greater than or equal to 1 and less than oe equal to 18 - Important
if (age >= 1) and (age <= 18):
    print("Imprtant to the future")
# If age is either 21 or 50 - Important
elif (age == 21) or (age == 50):
    print("Rare breed on the earth")
# Check if age is less than 65 and then convert true to false and vice versa
elif not (age < 65):
    print("Makers of the present, protect at all costs")
# Else not important
else:
    print("You're amazing but not important at the moment")