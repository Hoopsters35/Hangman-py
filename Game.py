from Answer import Answer
from Illustration import Illustration
def playAgain():
	inp = input("Would you like to play again [Y/N] ")
	while inp.upper() != 'Y' or inp.upper() != "N":
		print('Please use the given format.')
		inp = input("Would you like to play again [Y/N] ")
	if inp.upper() == 'Y':
		return True
	else: return False

play_again = True
while play_again:
	tmp = input('Enter a word to guess! ')
	answer = Answer(tmp)
	while answer.cont():
		answer.getGuess()
		answer.checkGuess()
		answer.displayToPlayer()




	playAgain()
print('Goodbye!')
