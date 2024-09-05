def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True    
#prime
n=int(input())
flag=is_prime(n)
if(flag==True):
    print("prime Number")
else:
    print("not prime")
    