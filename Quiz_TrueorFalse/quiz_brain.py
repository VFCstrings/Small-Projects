class QuizBrain:
	def __init__(self, q_list):
		self.question_number=0
		self.my_score = 0
		self.question_list=q_list


	def next_question(self):
		while self.still_questions()=="True":
			question=self.question_list[self.question_number]
			question_text=question.question
			question_category=question.category
			question_difficulty=question.difficulty
			question_answer=question.answer
			answer=input(print(f"Q {self.question_number+1}. The category is {question_category}. The difficulty is {question_difficulty}. Here we go...\n{question_text}. True or False"))
			print
			self.score_tracker(answer, question.answer)

	def score_tracker(self, answer, question_answer):
		answer = answer.lower()
		question_answer=question_answer.lower()
		if answer == question_answer:
			print("You are right! Well done :)")
			print()
			self.my_score+=1
		else:
			print("Oh... That is wrong...")
			print()
			self.my_score+=0

		print(f"The correct answer was {question_answer}")
		print(f"Your total score is {self.my_score}/{self.question_number+1}")
		print()
		self.question_number += 1

	def still_questions(self):
		if self.question_number<len(self.question_list):
			return "True"
		else:
			"False"
			print("That's the end of this Quiz!")
			print(f"You\'r final score is {self.my_score}")
			exit()
