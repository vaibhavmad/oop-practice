class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.enrolled_classes = []
    
    def enroll_class(self, teacher):
        if teacher.subject not in self.enrolled_classes:
            print(f"{self.name} enrolled in {teacher.name}'s {teacher.subject} class.")
            self.enrolled_classes.append(teacher.subject)
        else:
            print(f"{self.name} is already enrolled in {teacher.name}'s {teacher.subject} class.")
            
    def my_classes(self):
        if self.enrolled_classes:
            print(f"--- {self.name}'s Enrolled Classes ---")
            for subject in self.enrolled_classes:
                print(subject)
        else:
            print(f"{self.name} has not enrolled in any classes as of now.")
            