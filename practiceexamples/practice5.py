#program to count the number of strings where the string length is 2 or more and the first and last character are same
# from a given list of strings.
	#	Sample List : ['abc', 'xyz', 'aba', '1221']
	#	Expected Result : 2

lst=[val for val in input().split()]
def count_func(lst):
    count = 0
    for str in lst:
        if(len(str)<2):
            print("you entered the string which has the length below 2 , please enter the string where the length more than 2 ",str)
            print("="*50)
        else:
            if(str[0]==str[-1]):
                count+=1
    print("original list of strings ",lst)
    print("no of strings having first and last character are same from the  give list of strings: ",count)
count_func(lst)