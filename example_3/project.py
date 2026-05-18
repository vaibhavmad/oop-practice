class Project:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.assigned_employee_list = []
        self.used_budget = 0
        
    def project_report(self):
        if self.assigned_employee_list:
            print(f"--- {self.name} Team Report ---")
            for employee in self.assigned_employee_list:
                print(f"Name: {employee.name} | Role: {employee.role} | Salary: {employee.salary}")
            print(f"Total Salary Cost: {self.used_budget} / Budget: {self.budget}")
        else:
            print("Project not started yet.")
        