class Employee:
    company = "Google"
    salary = 100

Rayhan = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# Rayhan.salary = 300
# rajni.salary = 400
Rayhan.salary = 45
print(Rayhan.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 