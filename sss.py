def calculate(N,Arr):
    ard = []
    ar=[]
    vis = [False for i in range(N)]
    for i in range(N):
        if(vis[i]==True):
            continue
        count = 1
        for j in range(i+1,N,1):
            if(Arr[i]==Arr[j]):
                vis[j]=True
                count +=1
        if count ==1:
            #print(Arr[i])
            ar.append(Arr[i])
    ans=len(ar)
    for i in Arr:
        if(Arr[i]>=3):
            mm=Arr.index(Arr[i])
            Arr.remove(Arr[mm])
    if N >=7:
        myset =set(Arr)
        Arr.remove(Arr[0])
    ans=len(Arr)
    return ans

#mainprogram
N=int(input())
Arr = [int(val) for val in input().split(",")]
ans=calculate(N,Arr)
print(ans)


"""
This code takes an input of a number N and a list of integers Arr. 
It initializes an empty list ard, an empty list ar, and a list of False values with a length of N.
 It then iterates through the Arr list and checks if the current index has been visited before (by checking the corresponding index in the vis list). 
 If it has, it continues to the next index. If not, it counts the number of occurrences of that element in the Arr list,
  marks all those indices as visited, and appends the element to the ar list if the count is 1.

The code then sets the variable ans to the length of the ar list, and removes all elements of the Arr list with a value greater than or equal to 3. 
If N is greater than or equal to 7, the code converts the Arr list to a set and removes the first element of the Arr list. 
Finally, the code sets ans to the length of the Arr list, and returns it.

This code will check the input list of integers and calculate the length of the list after removing the element that occurs more than once,
 also check if N is greater than 7 then it will remove the first element of the list and return the length of the list, and print it as the final output.
"""