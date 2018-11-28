from IPython.display import clear_output

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
def player_input():
    """
    OUTPUT= (Player1 marker, Player2 marker)
    """
    
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player1: Choose X or O : ').upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
def place_marker(board, marker, position):
    
    board[position]=marker  
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
  
import random

def choose_first():
    
    flip= random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'           
def space_check(board, position):
    
    return board[position]==''        
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True  
def player_choice(board):
    
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position: (1-9)'))
        
    return position    
def replay():
    
    choice=input('Play again? Enter Yes or No : ')
    
    return choice=='Yes'          
# while loop to keep running the game
print('Welcome to Tic Tac Toe!')

while True:
    # Play the game
    # Set the game up here
    #pass
    the_board=['']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn + ' will go first')
    
    play_game=input('Ready to play? Y or N : ')
    
    if play_game =='y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
         #Player 1 Turn
        if turn=='Player 1':
            
            display_board(the_board) # show the board
            
            #choose a position
            position=player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            #Check if the won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON !!')
                game_on = False
            else:   #or check if there is a tie?
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME TIED !!')
                    game_on = False
                else: 
                    turn='Player 2'
            
        #No tie and no win then next player's turn
         # Player2's turn.
        else: 
            display_board(the_board) # show the board
            
            #choose a position
            position=player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            #Check if the won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON !!')
                game_on = False
            else:   #or check if there is a tie?
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME TIED !!')
                    game_on = False
                else: 
                    turn='Player 1'
                    

    if not replay():
        break
    # Break out of the while loop on replay()        