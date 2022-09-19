"""
CSE 210
Wk01 Tic Tac Toe 
Stacie Abbey

X - The program must have a comment with assignment and author names.
X - The program must have at least one if/then block.
X - The program must have at least one while loop.
X - The program must have more than one function.
X - The program must have a function called main.
"""
# Game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# Current player
current_player = 'X'

# Check for if game is continuing
game_running = True

# Run the game
def main():
    while game_running:
        print_board(board)
        player_input(board)
        check_for_winner()
        check_for_draw(board)
        switch_player()

# print game board
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# take player input
def player_input(board):
    player_choice = int(input('Enter a number between 1-9: '))
    if player_choice >= 1 and player_choice <= 9 and board[player_choice - 1] == '-':
        board[player_choice - 1] = current_player
    else:
        print('Try Again. Spot is taken.')

# check rows, columns, and diagonal for win
def winner(board):
            # checking rows
    return (board[0] == board[1] == board[2] and board[1] != '-' or
            board[3] == board[4] == board[5] and board[3] != '-' or
            board[6] == board[7] == board[8] and board[6] != '-' or
            # checking columns
            board[0] == board[3] == board[6] and board[0] != '-' or
            board[1] == board[4] == board[7] and board[1] != '-' or
            board[2] == board[5] == board[8] and board[2] != '-' or
            # checking diagonals 
            board[0] == board[4] == board[8] and board[0] != '-' or
            board[2] == board[4] == board[6] and board[2] != '-')
       
# Check for draw
def check_for_draw(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print('This Game has resulted in a draw. Try again!')  
        game_running = False   

# switch player
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else :    
        current_player = 'X'

# Check to see if winner has been found and if so display winner and stop game
def check_for_winner():
    global game_running
    if winner(board):
        print_board(board)
        print(f'{current_player} has won!')
        game_running = False


# Call main to start this program.
if __name__ == "__main__":
    main()
