def add_numbers(num1, num2):
    """ 
    This function calculates the sum of two numbers and returns the result.
    """
    sum_result = num1 + num2
    return sum_result

# Prompt the user to enter two numbers and store them as integers.
user_num1 = int(input("Enter the first number: "))
user_num2 = int(input("Enter the second number: "))

# Calculate the sum of the user-provided numbers using the add_numbers function.
result = add_numbers(user_num1, user_num2)

# Display the sum to the user.
print(f"The sum of {user_num1} and {user_num2} is {result}")
