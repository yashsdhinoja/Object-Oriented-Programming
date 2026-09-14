# Create a class 'Employee' that keeps track of how many Employee objects have been created using a class attribute.

class Employee:
    count = 0

    def __init__(self,employee):
        self.employee = employee
        Employee.count += 1

E1 = Employee("qwerty")
E2 = Employee("Alex")
E3 = Employee("Tejas")

print(f"Total Employees : {Employee.count}")