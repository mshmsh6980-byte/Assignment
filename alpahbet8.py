employees = []
empln = int(input("Enter number of employees: "))


for i in range(emplnum):
    name = input(f"Enter name {i+1}: ")
    employees.append(name)
employees.sort()


print("Sorted employee names:")
for name in employees:
    print(name)
print(employees)