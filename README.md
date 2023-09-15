# EASY: 004 Python - Sum of Two Numbers

## Description

Create a function that takes two numbers as arguments and return their sum.

## Sample Solution

```python
def sum_two_numbers(a, b):
    return a + b
```

## Examples

### Example 1

```text
Input: `add_numbers(5, 7)`
Output: `12`
Explanation: The sum of 5 and 7 is 12.
```

### Example 2

```text
Input: `add_numbers(-3, -4)`
Output: `-7`
Explanation: The sum of -3 and -4 is -7.
```

### Example 3

```text
Input: `add_numbers(10, -3)`
Output: `7`
Explanation: The sum of 10 and -3 is 7.
```

## Constraints

- None

## Testing

NOTE: Make sure you're in the `004-python-sum-of-two-numbers` directory (containing the `test.py` file) when executing the command above.

- To navigate to the directory containing the test file from the current terminal, run the following command:

```bash
cd scr/
```

- Then run the following command in a terminal to test your code:

```bash
python -m unittest -v test
```

- And make sure you get the following output:

```bash
test_add_mixed_numbers (test.TestAddNumbers.test_add_mixed_numbers) ... ok
test_add_negative_numbers (test.TestAddNumbers.test_add_negative_numbers) ... ok
test_add_positive_numbers (test.TestAddNumbers.test_add_positive_numbers) ... ok

# Sum of Two Numbers

Creating a function that takes two numbers as arguments and return their sum.

## Function: `add_numbers(a, b)`

This function adds two numbers and returns the result.

### Parameters

- `a` (int or float): The first number to be added.
- `b` (int or float): The second number to be added.

### Returns

- int or float: The sum of the two input numbers.

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
