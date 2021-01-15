num1=input("enter first number")
num2=input("enter second number")
result=float(num1)/float(num2)
print(result)
if (float(num1) % float(num2))==0:
    print( num1,"is multiple of",num2)
else:
    print(num1,"is not multiple of",num2)
