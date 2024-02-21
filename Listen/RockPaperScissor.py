import random
elements = ['rock', 'paper', 'scissor']
print('0 = Rock, 1 = Paper, 2 = Scissor')
player = input('Enter your choice: ')
if player == '0':
    player = 'rock'
elif player == '1':
    player = 'paper'
elif player == '2':
    player = 'scissor'
else:
    print('Invalid input')
    exit()

AI = elements[random.randint(0, 2)]
print('AI: ', AI)
if player == AI:
    print('Draw')
elif player == 'rock' and AI == 'scissor':
    print('Player wins')
elif player == 'scissor' and AI == 'paper':
    print('Player wins')
elif player == 'paper' and AI == 'rock':
    print('Player wins')
else:
    print('AI wins')
