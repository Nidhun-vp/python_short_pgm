def find_second_large(mylist):
    unique_list=list(set(mylist))
    unique_list.sort()
    return unique_list[-2] if len(unique_list)>=2 else None
mylist=[10,20,30,50,60,7,78,2,6]
result=find_second_large(mylist)
print("second Large is:",result)