print('Rock.....')
print('Paper....')
print('Scissors...')

player1= input('Player1 make your move: ')
print("***NO CHEATING!\n\n" * 20)
player2= input('Player2 make your move: ')

if player1 ==  player2 :
     print('Its a TIE')	
elif player1 == 'rock': 
    if player2 == 'paper':  
	     print('Player2 WINS!')
    elif player2 == 'scissors':
         print('Player1 WINS!')
elif player1 == 'paper': 
    if player2 == 'rock':
	     print('Player1 WINS!')
    elif player2 == 'scissors':
         print('Player2 WINS!')
elif player1 == 'scissors': 
     if player2 == 'paper':
	     print('Player1 WINS!')
     elif player2 == 'rock':
	     print('Player2 WINS!')			
else:
	print("something went wrong")