# Create a function that takes two numbers as arguments and return their sum.

# Example 1.
# Input: `add_numbers(5, 7)`
# Output: `12`
# Explanation: The sum of 5 and 7 is 12.

# Example 2.
# Input: `add_numbers(-3, -4)`
# Output: `-7`
# Explanation: The sum of -3 and -4 is -7.

# Constrains: NONE

def sum_two_numbers(num1, num2):
    """ Return the sum of two values """
    answer = num1 + num2
    return answer

user_num1 = int(float("first number: "))
user_num2 = int(float("Second number: "))
print(f"The sum of {user_num1} and {user_num2} is {sum_two_numbers(user_num1,user_num2)}")
