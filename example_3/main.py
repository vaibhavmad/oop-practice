from employee import Employee
from project import Project

employee_1 = Employee("Vaibhav", "AI Engineer", 80000)
employee_2 = Employee("Rahul", "Designer", 60000)
employee_3 = Employee("Priya", "Manager", 90000)

project_1 = Project("AI Dashboard", 300000)
project_2 = Project("Mobile App", 200000)

project_1.project_report()
employee_1.my_projects()

employee_1.assign_project(project_1)
employee_2.assign_project(project_1)
employee_1.assign_project(project_1)
employee_3.assign_project(project_1)

employee_1.assign_project(project_2)
employee_2.assign_project(project_2)
employee_3.assign_project(project_2)
employee_2.assign_project(project_2)

employee_1.my_projects()
employee_2.my_projects()
employee_3.my_projects()

project_1.project_report()
project_2.project_report()