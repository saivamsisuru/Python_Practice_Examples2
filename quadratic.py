#Evaluation of qudratic equation and getting the roots of the equation
import math

a=float(input("enter a coefficient: "))
b=float(input("enter b coefficient: "))
c=float(input("enter constant: "))

d=(b**2)-(4*a*c)
x=round((-b-math.sqrt(d))/(2*a),2)
y=round((-b+math.sqrt(d))/(2*a),2)
print("{} is root".format(x))
print("{} is another root".format(y))

