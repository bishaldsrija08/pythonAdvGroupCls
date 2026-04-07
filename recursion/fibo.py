# 0 1 1 2 3 5 8 13 21 34 55 89 144
# WAP to find the nth term of the Fibonacci sequence using recursion



def fibo(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter the term number: "))
print(f"The {n}th term of the Fibonacci sequence is: {fibo(n)}")