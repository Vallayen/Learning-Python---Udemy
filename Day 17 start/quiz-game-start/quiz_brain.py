class QuizzBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank

    def start_quiz(self):
        score = 0
        for question in self.questions_list:
            user_answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)? ")
            if user_answer.lower() == question.answer.lower():
                print("That's correct!")
                score += 2
            else:
                print("Sorry, that's not correct.")
            self.question_number += 1
        print(f"Your Score is {score}/{self.question_number}")