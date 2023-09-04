# Store user input of 2 numbers and operator of choice
num1, operator, num2 = input("Enter calculation seperated by a space ").split()
# Convert strings to integer
num1 = int(num1)
num2 = int(num2)
# Perform the required operation
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Input valid operator: +, -, *, or /")
# Print result