class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def calc_avg(self):
        total = 0
        for mark in self.__marks.values():
            total += mark
        avg = total / len(self.__marks)
        return avg

    def is_passed(self):
        has_passed = all(mark >= 35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} has Passed")
        else:
            print(f"{self.name} has Failed")

    def calc_grade(self):
        percentage = self.calc_avg()
        print("Grade:", end=" ")

        if percentage >= 90:
            print("A")
        elif percentage >= 85:
            print("B")
        elif percentage >= 70:
            print("C")
        elif percentage >= 50:
            print("D")
        else:
            print("F")


class Report_card:
    @staticmethod
    def generate(student: Student):
        student_marks = student.get_marks()

        print(f"\nName : {student.name}\t Roll No : {student.roll_no}")
        print("------------------------------")

        for subject, marks in student_marks.items():
            print(f"{subject} - {marks}")

        print("------------------------------")
        print(f"Average : {student.calc_avg():.2f}")

        student.is_passed()
        student.calc_grade()


# --------- Main Program ---------
anu = Student(10, "Ananya")
anu.add_marks("Math", 94)
anu.add_marks("Dancing", 34)

Report_card.generate(anu)