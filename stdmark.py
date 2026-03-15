from  encodings.aliases import aliases
from tkinter.font import names
stdmark=[]
passedstd=[]
for i in range(3):
    names=str(input("Enter your name: "))
    mark=int(input("Enter your marks: "))

    stdmark.append(names)
    stdmark.append(mark)
    if mark >= 50:
        passedstd.append(names)
        passedstd.append(mark)
        print("passed")
    else:
        print("not passed")
print("---")
print("stdmark: ")
print(stdmark)
print("---")
print("passedstd: ")
print(passedstd)
print("---")


print(stdmark.insert(3,"ali"))
print(stdmark.insert(3,44))
print(stdmark)
print("---")
stdmark[2]="ahmed"
print(stdmark)


