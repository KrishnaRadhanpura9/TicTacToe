board = [' ' for _ in range(9)]  # Create a list to represent the game board

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def play_game():
    player = 'X'
    while True:
        print_board()
        move = input(f"Player {player}, please select a position (1-9): ")
        try:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = player
                if check_winner():
                    print_board()
                    print(f"Congratulations, player {player} has won!")
                    break
                if check_tie():
                    print_board()
                    print("It's a tie!")
                    break
                player = 'O' if player == 'X' else 'X'
            else:
                print("That position is already occupied, please choose another one.")
        except ValueError:
            print("Invalid input, please enter a number between 1 and 9.")

def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

def check_tie():
    return ' ' not in board

play_game()  # Start the game
