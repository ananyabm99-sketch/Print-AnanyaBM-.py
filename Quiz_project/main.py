from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(question_text,question_answer)   #Question(q_text = question_text,q_answer = question_answer)=named parametrs
    question_bank.append(new_q)
#print(question_bank)

quiz = Quiz_brain(question_bank)
while quiz.still_ask_question():
    quiz.next_question()
    quiz.final_score()
print("Well done you completed the quiz!")
quiz.Total_score()