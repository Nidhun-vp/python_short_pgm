def count_vowel(s):
    return sum(1 for char in s.lower() if char in 'aeiou')
s=input("enter a text:")   
result=count_vowel(s)
print("count of vowels in given text is:",result)