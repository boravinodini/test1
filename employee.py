def task_logger(func):
    def wrapper(self, task_name):
        print("Task assignment started...")
        func(self, task_name)
        print("Task assignment completed.")

    return wrapper

class Employee:
    company_name = "TechSolutions"

    def __init__(self, name, employee_id, salary):
        # Instance variables
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    def display_details(self):
        print("\nCompany:", self.company_name)
        print("Employee:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print("\nCompany name updated to", cls.company_name)

    @staticmethod
    def validate_salary(salary):
        if salary > 0:
            return True
        else:
            return False

class Developer(Employee):

    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(
            self.name,
            "is writing code using",
            self.programming_language + "."
        )

class ProjectManager(Employee):

    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    @task_logger
    def assign_task(self, task_name):

        if task_name.strip() == "":
            print("Invalid task name. Task cannot be empty.")
        else:
            print("Task assigned:", task_name)


dev1 = Developer("Ravi","E101",40000, "Python")
dev2 = Developer("Dhanu","E102",45000,"Java")
manager = ProjectManager("Vinnu","E103",70000,5)
print("========== EMPLOYEE DETAILS ==========")

dev1.display_details()
dev2.display_details()
manager.display_details()

print("\n========== DEVELOPERS ==========")
dev1.write_code()
dev2.write_code()
print("\n========== TASK ASSIGNMENT ==========")
manager.assign_task("Develop login page")
print("\n========== COMPANY UPDATE ==========")
Employee.change_company_name("CodeCraft Solutions")
print("\nUpdated company name for all employees:")
print(dev1.name, "->", dev1.company_name)
print(dev2.name, "->", dev2.company_name)
print(manager.name, "->", manager.company_name)
print("\n========== SALARY VALIDATION ==========")
negative_salary = -5000
if Employee.validate_salary(negative_salary):
    print("Salary is valid")
else:
    print("Invalid salary:", negative_salary)
valid_salary = 50000
if Employee.validate_salary(valid_salary):
    print("Valid salary:", valid_salary)
else:
    print("Invalid salary:", valid_salary)
print("\n========== EMPTY TASK VALIDATION ==========")
manager.assign_task("")
print()
emp1 = Employee("Anu","E104",30000)
emp2 = Employee("Priya","E105", 60000)
emp1.display_details()
emp2.display_details()
print("\nEmployee data is independent:")
print(emp1.name, "Salary:", emp1.salary)
print(emp2.name, "Salary:", emp2.salary)








