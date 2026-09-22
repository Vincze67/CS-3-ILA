class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"


class Course:
    def __init__(self, course_code: str, course_name: str):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Only instances of Student can be added.")

    def list_students(self):
        print(f"Students enrolled in {self.course_name} ({self.course_code}):")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")


if __name__ == "__main__":
    python_course = Course("CS101", "Introduction to Python")

    student1 = Student("S001", "Alice")
    student2 = Student("S002", "Bob")

    python_course.add_student(student1)
    python_course.add_student(student2)

    python_course.list_students()