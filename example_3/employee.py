class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.project_list = []
        
    def assign_project(self, project):
        if project.budget > self.salary + project.used_budget:
            if self not in project.assigned_employee_list:
                print(f"{self.name} assigned to {project.name}.")
                self.project_list.append(project.name)
                project.assigned_employee_list.append(self)
                project.used_budget += self.salary
            else:
                print(f"{self.name} already assigned to {project.name}.")
        else:
            print(f"Budget exceeded. Can not assign {self.name} to {project.name}.")
            
    def my_projects(self):
        if self.project_list:
            print(f"--- {self.name}'s Projects ---")
            for name in self.project_list:
                print(name)
        else:
            print(f"No projects assigned to {self.name} yet.")