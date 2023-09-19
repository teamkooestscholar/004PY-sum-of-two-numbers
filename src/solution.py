def add_numbers():
    while True:
        num1_input = input("Enter the first number (or 'q' to quit): ")
        if num1_input.lower() == 'q':
            break
        
        num2_input = input("Enter the second number (or 'q' to quit): ")
        if num2_input.lower() == 'q':
            break
        
        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
            
            sum_result = num1 + num2
            print(f"The sum of {num1} and {num2} is: {sum_result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers or 'q' to quit.")

add_numbers()