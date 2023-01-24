#program to find the list of words that are longer than n from a given list of words
lst=[val for val in input().split()]
def function(lst):
    n=int(input("enter the expecting length of the word: "))
    longlst = []
    for word in lst:
        if(len(word)>n):
            longlst.append(word)
    return longlst
longlst=function(lst)
print(longlst)
