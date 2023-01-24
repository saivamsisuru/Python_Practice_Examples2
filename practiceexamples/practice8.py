#program to check a list is empty or not
lst=[val for val in input().split()]
if(len(lst)==0):
    print("given list is empty and the list=",lst)
else:
    print("given list is non empty and the list=",lst)

#by using ternary operator
#print("given list is empty and the list=",lst) if(len(lst)==0) else print("given list is non empty and the list=",lst)
