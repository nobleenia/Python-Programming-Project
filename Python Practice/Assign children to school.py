# Enter age and convert to integer
age = eval(input("Enter your age: "))
# If age is less than 5, got to daycare or not ready for school
if (age < 5):
    print("Go to daycare or stay at home with your parents") 
# If age is 5, go to kidergarten
elif (age == 5):
    print("Go to kindergarten")
# Ages 6 through 17 goes to grade 1 through 12
elif (age >= 6) and (age <= 17):
    print("Go to grade {}".format(age - 5))
# If age is greater than 17 go to college
elif (age > 17):
    print("Go to college")
