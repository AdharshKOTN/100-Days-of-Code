from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

QB = QuizBrain(question_bank)
score = 0
while QB.question_number < len(QB.question_list):
    score += QB.nextQuestion()
    print(f"Score: ({score}/{len(question_bank)})")
