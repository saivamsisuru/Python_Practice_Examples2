print("="*50)
#converting kilometres into miles
km=float(input("enter distance in kilometres: "))
conv_fac=0.621371
miles=km*conv_fac
print("{}km in {}miles".format(km,miles))
print("="*50)
#converting miles into kilometres
miles1=float(input("enter distance in miles: "))
km1=miles/conv_fac
print("{}miles in {}km".format(miles1,km1))
print("="*50)