from math import factorial
fact=int(input("enter a factorial"))
for i in range(fact-1,0,-1):
    fact=fact*i
print(fact)