import random

def game_even():
	print('VD-even\nWelcome to the VD-games!')
	name = input('May I have your name? ')
	print(f'Hello, {name}')
	print('Answer "yes" if the number is even, otherwise answer "no".')
	correct_answers = 0
	while correct_answers < 3:
		number = random.randint(1,100)
		print(f'Question: {number}')
		answer = input ('Your answer: ').strip().lower()
		correct_answer = "yes" if number % 2 == 0 else "no"
		if answer != correct_answer:
			print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
			print(f"Let's try again, {name}!")
			continue
		else:
			print('Correct!')
			correct_answers += 1
	if correct_answers == 3:
		print(f'Congratulations, {name}!')
