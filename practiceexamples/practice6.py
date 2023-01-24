#Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last(n): return n[-1]
def sort_func(lst):
    print("sorted list=",sorted(lst,key=last,reverse=False))

#main method
firstvalues=[int(val) for val in input().split()]
sceondvalues=[int(val) for val in input().split()]
c=list(zip(firstvalues,sceondvalues))
print("given list= ",c)

sort_func(c)
