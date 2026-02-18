def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ": return True
        if board[0][i] == board[1][i] == board[2][i] != " ": return True
    if board[0][0] == board[1][1] == board[2][2] != " ": return True
    if board[0][2] == board[1][1] == board[2][0] != " ": return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = "X"
    for move in range(9):
        print_board(board)
        print(f"Player {turn}'s turn.")
        try:
            row, col = map(int, input("Enter row and col (0-2) separated by space: ").split())
            if board[row][col] == " ":
                board[row][col] = turn
                if check_winner(board):
                    print_board(board)
                    print(f"Player {turn} wins!")
                    return
                turn = "O" if turn == "X" else "X"
            else:
                print("Cell already taken!")
        except:
            print("Invalid input! Use format: 0 0")
    print("It's a tie!")

if __name__ == "__main__":
    main()