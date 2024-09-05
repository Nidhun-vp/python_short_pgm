def fibonacci(n):
    fib_sequence=[0,1]
    while len(fib_sequence)<n:
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence[:n]   
n=int(input("enter limit of fibonacci you want to print:"))
result=fibonacci(n)
print(result) 