class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.attendance_report = {}
        
    def mark_attendance(self, student, attendance):
        if self.subject in student.enrolled_classes:
            self.attendance_report[student.name] = attendance
            print("Attendance Marked.")
        else:
            print(f"{student.name} is not enrolled in {self.name}'s class.")
            print("Can not mark attendance.")
        
    def attendance_status(self):
        if self.attendance_report:
            print(f"--- {self.name}'s attendace report ---")
            for key, value in self.attendance_report.items():
                print(f"{key}: {value}")
        else:
            print("Attendance not recorded yet.")