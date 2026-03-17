x=int(input("enter the number:"))
primefound=True
if x>1:
    for i in range(2,x):
        if (x%i)==0:
            primefound=False
            break
if primefound:
    print(x,"is a prime number")
else:
    print(x,"is not a prime number")
