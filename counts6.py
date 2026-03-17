N=int(input("enter a integer"))
count=0
while N!=0:
    N//=10
    count+=1
print(count)

