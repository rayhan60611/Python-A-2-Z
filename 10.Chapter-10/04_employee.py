class Employee:
    company = "Google"
    salary = 100

Rayhan = Employee()
rajni = Employee()
Rayhan.salary = 300
rajni.salary = 400

print(Rayhan.company)
print(rajni.company)
Employee.company = "YouTube"
print(Rayhan.company)
print(rajni.company)
print(Rayhan.salary)
print(rajni.salary)