class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, name, age, grade)
            print(f"Student {name} added successfully.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} deleted successfully.")
        else:
            print(f"No student found with ID {student_id}.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self.students:
            if name:
                self.students[student_id].name = name
            if age:
                self.students[student_id].age = age
            if grade:
                self.students[student_id].grade = grade
            print(f"Student with ID {student_id} updated successfully.")
        else:
            print(f"No student found with ID {student_id}.")

    def view_students(self):
        if self.students:
            for student_id, student in self.students.items():
                print(student)
        else:
            print("No students available.")

    def view_student(self, student_id):
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print(f"No student found with ID {student_id}.")
sms = StudentManagementSystem()

# Adding students
sms.add_student(1, "Alice", 20, "A")
sms.add_student(2, "Bob", 21, "B")

# Viewing all students
sms.view_students()

# Viewing a specific student
sms.view_student(1)

# Updating a student
sms.update_student(1, age=21, grade="A+")

# Deleting a student
sms.delete_student(2)

# Viewing all students after deletion
sms.view_students()
