# Lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# The syntax of a lambda function is: lambda arguments: expression


square = lambda x: x ** 2
result = square(5)  # Output: 25
print(result)