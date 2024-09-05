def gcd(a,b):
    while b:
        a,b=b,a%b
        return a
a=int(input())
b=int(input())    
result=gcd(a,b)
print("greatest common divisor:",result)