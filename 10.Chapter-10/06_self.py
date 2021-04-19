class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

Rayhan = Employee()
Rayhan.salary = 100000
Rayhan.getSalary() # Employee.getSalary(Rayhan)