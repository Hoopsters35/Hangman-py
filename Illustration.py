class Illustration:

	def __init__(self):
		self.numGuesses = 0

	def setGuess(self, n):
		self.numGuesses = n

	def add_guess(self):
		self.numGuesses += 1

	@staticmethod
	def getIllustration(num):
		if num == 0:
			Illustration.illustration0()
		elif num == 1:
			Illustration.illustration1()
		elif num == 2:
			Illustration.illustration2()
		elif num == 3:
			Illustration.illustration3()
		elif num == 4:
			Illustration.illustration4()
		elif num == 5:
			Illustration.illustration5()
		elif num == 6:
			Illustration.illustration6()
		elif num == 7:
			Illustration.illustration7()

	def illustration0(self):
		print(" ____________________  ")
		print("/                     \\")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print(" \\____________________/")

	def illustration1(self):
		print(" ____________________  ")
		print("/         ___         \\")
		print("|       /     \\       |")
		print("|      |       |      |")
		print("|       \\_____/       |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print("|                     |")
		print(" \\____________________/")

	def illustration2(self):
		print(" ____________________  ")
		print("/         ___         \\")
		print("|       /     \\       |")
		print("|      |       |      |")
		print("|       \\_____/       |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|                     |")
		print("|                     |")
		print(" \\____________________/")

	def illustration3(self):
		print(" ____________________  ")
		print("/         ___         \\")
		print("|       /     \\       |")
		print("|      |       |      |")
		print("|       \\_____/       |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|           \\         |")
		print("|            \\        |")
		print(" \\____________________/")

	def illustration4(self):
		print(" ____________________  ")
		print("/         ___         \\")
		print("|       /     \\       |")
		print("|      |       |      |")
		print("|       \\_____/       |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|          |          |")
		print("|         / \\         |")
		print("|        /   \\        |")
		print(" \\____________________/")

	def illustration5(self):
		print(" ____________________  ")
		print("/         ___         \\")
		print("|       /     \\       |")
		print("|      |       |      |")
		print("|       \\_____/       |")
		print("|          |  /       |")
		print("|          | /        |")
		print("|          |/         |")
		print("|          |          |")
		print("|          |          |")
		print("|         / \\         |")
		print("|        /   \\        |")
		print(" \\____________________/")

	def illustration6(self):
		print(" ____________________  ")
		print("/         ___         \\")
		print("|       /     \\       |")
		print("|      |       |      |")
		print("|       \\_____/       |")
		print("|       \\  |  /       |")
		print("|        \\ | /        |")
		print("|         \\|/         |")
		print("|          |          |")
		print("|          |          |")
		print("|         / \\         |")
		print("|        /   \\        |")
		print(" \\____________________/")

	def illustration7(self):
		print(" ____________________  ")
		print("/         ___         \\")
		print("|       / . . \\       |")
		print("|     (| \___/ |)     |")
		print("|       \\_____/       |")
		print("|       \\  |  /       |")
		print("|        \\ | /        |")
		print("|         \\|/         |")
		print("|          |          |")
		print("|          |          |")
		print("|         / \\         |")
		print("|        /   \\        |")
		print(" \\____________________/")

