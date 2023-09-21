def sum_two_numbers(num1, num2):
    """ Return the sum of two values """
    answer = num1 + num2
    return answer

user_num1 = int(float("first number: "))
user_num2 = int(float("Second number: "))
print(f"The sum of {user_num1} and {user_num2} is {sum_two_numbers(user_num1,user_num2)}")