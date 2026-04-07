# 5! = 5 x 4 x 3 x 2 x 1
# 10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
# 1! or 0! = 1

"""
fact = 1
for i in range(1, 11, 1):
    fact = fact * i
print(fact)
"""

# WAP to find the factorial of a number using recursion

def factorial(n):
    # base case
    if n ==0 or n==1:
        return 1
    return n * factorial(n-1) # recursive case