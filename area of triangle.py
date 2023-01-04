#program for finding the area of triangle
a=float(input("enter the side of triangle: "))
b=float(input("enter the side of triangle: "))
c=float(input("enter the side of triangle: "))
s=(a+b+c)/2
area_of_triangle=round((s*(s-a)*(s-b)*(s-c))**0.5,2)
print("area of triangle: {}".format(area_of_triangle))
