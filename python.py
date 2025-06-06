def add_three_numbers(num1, num2, num3):
  """Adds three numbers and returns the sum."""
  sum_of_numbers = num1 + num2 + num3
  return sum_of_numbers

# Example usage:
number1 = 10
number2 = 20
number3 = 30

result = add_three_numbers(number1, number2, number3)
print("The sum of the three numbers is:", result)  # Output: The sum of the three numbers is: 60

# Example with user input:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = add_three_numbers(num1, num2, num3)
print("The sum of the three numbers is:", result)
