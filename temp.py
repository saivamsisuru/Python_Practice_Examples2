print("="*50)
#program to convert celsius to fahrenheit
tc=float(input("enter the temperature in celsius: "))
tf=round((tc*1.8)+32,2)
print("{} degree celsius is equal to {} degree fahrenheit".format(tc,tf))
print("="*50)
#program to convert fahrenheit to celsius
tf1=float(input("enter the temperature in fahrenheit: "))
tc1=round((tf1-32)/1.8,2)
print("{} degree fahrenheit is equal to {} degree celsius".format(tf1,tc1))
print("="*50)
