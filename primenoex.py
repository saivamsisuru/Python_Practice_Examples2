#program to find the prime number of the given range
n=int(input("enter a number: "))
flag=False
for i in range(2,n):
    if (n%i)==0:
        flag=True
if flag:
    print("given number is not  PRIME NUMBER")
else:
    print("given number is PRIME NUMBER")
