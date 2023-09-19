# Create a function that takes two numbers as arguments and return their sum.

# Example 1:
# Input: `add_numbers(5, 7)`
# Output: `12`
# Explanation: The sum of 5 and 7 is 12.

# Example 2:
# Input: `add_numbers(-3, -4)`
# Output: `-7`
# Explanation: The sum of -3 and -4 is -7.

# Constraints: None

def add_numbers(num1, num2):
    """ 
    This function calculates the sum of two numbers and returns the result.
    """
    sum_result = num1 + num2
    return sum_result

# Ask the user to input two numbers and store them as integers.
user_num1 = int(input("Enter the first number: "))
user_num2 = int(input("Enter the second number: "))

# Calculate the sum of the user-provided numbers using the add_numbers function.
result = add_numbers(user_num1, user_num2)

# Display the sum to the user.
print(f"The sum of {user_num1} and {user_num2} is {result}")