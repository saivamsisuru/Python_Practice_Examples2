#program to sum all the items in a list
lst=[int(val) for val in input().split()]
def sum(lst):
    n=0
    for i in lst:
        n=n+i
    print(n)
sum(lst)