#function that takes two lists and returns True if they have at least one common member

def func():
    firstlst = [val for val in input().split()]
    secondlst = [val for val in input().split()]
    for word in firstlst:
        if(word in secondlst):
            return True
        else:
            return False
result=func()
print(result)