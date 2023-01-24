#program to multiply all the items in a list
lst=[int(val) for val in input().split()]
def mul(lst):
    n=1
    for i in lst:
        n=n*i
    print(n)
mul(lst)