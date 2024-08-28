from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

data=[]
for item in question_data:
	item_difficulty=item["difficulty"]
	item_category=item["category"]
	item_question=item["question"]
	item_answer=item["correct_answer"]
	new_question=Question(item_difficulty, item_category, item_question, item_answer)
	data.append(new_question)

QuizBrain(data).next_question()
QuizBrain(data).score_tracker()




