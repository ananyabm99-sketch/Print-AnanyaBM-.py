class Quiz_brain:
    def __init__(self, q_list, score=0):
        self.question_number = 0
        self.question_list = q_list
        self.score = score

    def still_ask_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(
            f"Q.{self.question_number}:{current_question.text}(True/False):"
        ).upper()
        self.check_answer(user_ans, current_question.answer.upper())

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            print("You are Right!")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer is {correct_ans}")

    def final_score(self):
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

    def Total_score(self):
        print(f"Your final score is {self.score}/{len(self.question_list)}")
