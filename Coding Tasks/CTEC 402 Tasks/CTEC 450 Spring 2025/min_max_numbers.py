# Program to find the minimum and maximum of five numbers

# Prompt the user to enter five numbers and store them in a list
numbers = []
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))  # Convert input to float for decimal support
    numbers.append(num)

# Determine the minimum and maximum values
min_num = min(numbers)
max_num = max(numbers)

# Display the results
print(f"\nThe minimum number is: {min_num}")
print(f"The maximum number is: {max_num}")
