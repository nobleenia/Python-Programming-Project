# Convert miles to kilometers
# Ask user to enter the number of miles they wish to convert
miles = input("Enter the number of miles you wish to convert ")
# Convert input to intt
miles = int(miles)
# Multiply the number recieved by 1.60934
kilometers = miles * 1.60934
# Print out the conversion in kilometers
print("{} miles equals {} kilometers" .format(miles, kilometers))