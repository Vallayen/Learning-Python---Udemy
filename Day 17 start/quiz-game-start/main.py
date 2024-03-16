from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain



question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    newq = Question(question_text, question_answer)
    question_bank.append(newq)
    


quiz_start = QuizzBrain(question_bank)
quiz_start.start_quiz()