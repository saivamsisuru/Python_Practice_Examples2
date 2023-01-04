#program to check whether the given year is leap year
year=int(input("enter the year: "))
#if(year%400==0) and  (year%100==0):
    #print("{} is leap year".format(year))
if(year%4==0) and (year%100 != 0):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))