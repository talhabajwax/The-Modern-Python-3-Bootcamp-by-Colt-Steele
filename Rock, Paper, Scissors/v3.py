import random
print('Rock.....')
print('Paper....')
print('Scissors...')

player= input('Player make your move: ')
rand_num =random.randint(0,2)
if rand_num == 0:
      computer ='rock'
elif rand_num ==1:
       computer ='paper'
else:
      computer ='scissors'
print(f'computer plays {computer}')
if player ==  computer :
     print('Its a TIE')	
elif player == 'rock': 
    if computer == 'paper':  
	     print('computer WINS!')
    elif computer == 'scissors':
         print('player WINS!')
elif player == 'paper': 
    if computer == 'rock':
	     print('Player WINS!')
    elif computer == 'scissors':
         print('computer WINS!')
elif player == 'scissors': 
     if computer == 'paper':
	     print('Player WINS!')
     elif computer == 'rock':
	     print('computer WINS!')			
else:
	print("something went wrong")