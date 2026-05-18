from student import Student
from teacher import Teacher

teacher_1 = Teacher("Mr. Sharma", "Mathematics")
teacher_2 = Teacher("Ms. Priya", "Science")

student_1 = Student("Arjun", 15)
student_2 = Student("Sneha", 14)

student_1.my_classes()
student_2.my_classes()

teacher_1.attendance_status()
teacher_2.attendance_status()

student_1.enroll_class(teacher_1)
student_2.enroll_class(teacher_2)

teacher_1.attendance_status()
teacher_2.attendance_status()

student_1.my_classes()
student_2.my_classes()

teacher_1.mark_attendance(student_1, "present")
teacher_2.mark_attendance(student_1, "absent")

teacher_1.mark_attendance(student_2, "absent")
teacher_2.mark_attendance(student_2, "present")

teacher_1.attendance_status()
teacher_2.attendance_status()