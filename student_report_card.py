class Student_data:

    def __init__(self, name, grade, student_id):
        self.name = name
        self.grade = grade
        self.student_id = student_id

    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Class : {self.grade}")
        print(f"Student ID : {self.student_id}")


class Marks_card(Student_data):

    def __init__(self, name, grade, student_id):
        super().__init__(name, grade, student_id)

    def subjects(self, m1, m2, m3, m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.average = (m1 + m2 + m3 + m4) / 4

    def calculate_grade(self):
        if self.average >= 35:
            return "A"
        elif self.average >= 25:
            return "B"
        elif self.average >= 20:
            return "C"
        else:
            return "Fail"

    def report_card(self):
        final_grade = self.calculate_grade()
        print("\n----- Report Card -----")
        print(f"Name : {self.name}")
        print(f"Class : {self.grade}")
        print(f"Student ID : {self.student_id}")
        print(f"Average : {self.average}")
        print(f"Final Grade : {final_grade}")


# Object
stud1 = Marks_card("Ananya", "12", "1234")
stud1.subjects(38, 34, 36, 35)
stud1.report_card()