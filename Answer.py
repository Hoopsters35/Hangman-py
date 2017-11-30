from Illustration import Illustration
class Answer:
	def __init__(self, word):
		self.answer = word
		self.guess = ""
		self.guesses = set()
		self.num_guesses = 0
		self.display_answer = self.generateDisplayAnswer()
		self.old_display_answer = self.generateDisplayAnswer()

	def generateDisplayAnswer(self):
		"""Generates a blank DisplayAnswer matching the style of the answer"""
		display_answer = []
		for i in self.answer:
			if not i == " ":
				display_answer += "_"
			else:
				display_answer += " "
		return display_answer

	def getGuess(self):
		"""Asks for guess input until guess length is == 1 and it hasn't been guessed yet"""
		self.guess = input('Enter a guess! ')
		while (not self.guess) or (len(self.guess) != 1) or (self.guess in self.guesses):
			print('Guess must be one character not previously guessed')
			self.guess = input('Enter a guess! ')

		self.guesses.add(self.guess)

	def updateDisplayAnswer(self):
		"""Runs the guess against the answer to update the display_answer"""
		counter = 0
		while counter < len(self.answer):
			if self.guess == self.answer[counter]:
				self.display_answer[counter] = self.answer[counter]
			counter += 1

	def checkGuess(self):
		""" Updates the DisplayAnswer if there are any instances of the guess in the answer. If not, increment num_guesses by 1 """
		self.updateDisplayAnswer()
		if self.display_answer == self.old_display_answer:
			num_guesses += 1
		else:
			self.old_display_answer = self.display_answer

	def displayToPlayer(self):
		#format answer here
		Illustration.getIllustration(self.num_guesses)
		print("{0}      {1}".format(self.display_answer, self.guesses))
		


	def cont(self):
		for i in range(len(self.answer)):
			if self.answer[i] != self.display_answer[i]:
				return True
		return False



