#program to display fibonacci sequence upto n-th term

def fibonacci(nterms=10):
    #nterms = int(input("enter the number of terms: "))
    if(nterms<=0):
        print("Invalid input")
    else:
        n1,n2=0,1
        i=0
        while(i<nterms):
            print("{}".format(n1))
            nth=n1+n2
            n1=n2
            n2=nth
            i=i+1

fibonacci()