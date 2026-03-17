num1=float(input("enter a number="))
num2=float(input("enter another number="))
num3=float(input("enter another number="))
if num1>num2 and num1>num3:
    print(str(num1)+" is greater")
elif num2>num1 and num2>num3:
    print(str(num2)+" is greater")
else:
    print(str(num3)+" is greater")