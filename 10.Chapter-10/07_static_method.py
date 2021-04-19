class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Rayhan = Employee()
Rayhan.salary = 100000
Rayhan.getSalary("Thanks!") # Employee.getSalary(Rayhan)
Rayhan.greet() # Employee.greet()
Rayhan.time()

