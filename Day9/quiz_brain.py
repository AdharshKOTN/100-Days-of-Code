class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def nextQuestion(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {next_question.text} (True/False): ")
        if answer == next_question.answer:
            print("That's the right answer!")
            return 1
        else:
            print("That's the wrong answer!")
            return 0
