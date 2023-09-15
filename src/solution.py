def add_numbers(a, b):
    result = a + b
    return result

a = input("Enter the 1st integer to add: ")
b = input("Enter the 2nd integer to add: ")

a=int(a)
b=int(b)

sum_result = add_numbers(a, b)
print("The sum of ",a , "and ",b , "is: " , sum_result)

