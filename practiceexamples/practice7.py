#program to remove duplicates from a list
lst=[val for val in input().split()]
#print(list((set(lst))))

print("given list=",lst)
def removeduplicates(lst):
    dlist=[]
    for val in lst:
        if(val in dlist):
            continue
        else:
            dlist.append(val)
    print("list of values where duplicates are not present=",dlist)
removeduplicates(lst)