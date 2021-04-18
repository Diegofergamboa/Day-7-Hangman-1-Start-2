import random
word_list = ["aardvark", "baboon", "camel"]

ran_choice = random.choice(word_list)
word_list = list(ran_choice)

#User_choice

user_choice = (input('Try to guess a letter: '))

#Algoritmo

for n in word_list :
	if n != user_choice :
		print('Keep trying')
		break
	else :
		print('Well done!')
		break
		
