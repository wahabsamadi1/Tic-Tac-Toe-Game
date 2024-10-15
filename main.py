# Tic-Tac-Toe Game

# Function to initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board(board):
    print("\n")
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full
def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to get the player's move
def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as integers from 0 to 2.")

# Function to play the game
def play_game():
    board = initialize_board()
    players = ['X', 'O']
    current_player = 0

    while True:
        display_board(board)
        player_move(board, players[current_player])

        if check_winner(board, players[current_player]):
            display_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if is_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 1 - current_player  # Switch player

if __name__ == "__main__":
    play_game()
