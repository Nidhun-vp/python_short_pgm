def merge_sorted_lists(list1,list2):
    return sorted(list1+list2)
list1=[1,2,3]
list2=[3,4,5]
result=merge_sorted_lists(list1,list2)
print(result)