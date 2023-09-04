# Ask user to input 2 values and store them in variables
num1, num2 = input("Enter two numbers seperated by a space ").split()
# Convert the strings to regular numbers, Integers
num1 = int(num1)
num2 = int(num2)
# Add the values entered and store in sum
sum = num1 + num2
# Subtract the values and store in diff
diff = num1 - num2
# Multiply the values and store in product
product = num1 * num2
# Divide the numbers and store in quotient
quotient = num1 / num2
# Use modulus on the values to find the remainder and store it in rem
rem = num1 % num2
#Print the results
print("The sum of {} and {} is {}" .format(num1, num2, sum))

print("The difference between {} and {} is {}" .format(num1, num2, diff))

print("The product of {} and {} is {}" .format(num1, num2, product))

print("The quotient of {} and {} is {}" .format(num1, num2, quotient))

print("The remainder of {} divided by {} is {}" .format(num1, num2, rem))