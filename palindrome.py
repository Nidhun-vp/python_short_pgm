def is_palindrome(s):
    return s==s[::-1]
s=input()
result=is_palindrome(s)
if(result==s):
    print("palindrome")
else:
    print("not palindrome")
print(result)