def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, ' '.join(row))


def player_move(board):
    while True:
        try:
            x = int(input("Enter X (0-2): "))
            y = int(input("Enter Y (0-2): "))
            if 0 <= x <= 2 and 0 <= y <= 2:
                if board[x][y] == ' ':
                    board[x][y] = 'X'
                    break
                else:
                    print("This cell is already taken..")
            else:
                print("Coordinates must be between 0-2.")
        except ValueError:
            print("Please enter numeric values.")


def computer_move(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == ' ':
                board[x][y] = 'O'
                print(f"The computer put an 'O' in position ({x}, {y})")
                return


def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False


def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-tac-toe game. You play as 'X'.")

    while True:
        print_board(board)
        player_move(board)
        if check_winner(board, 'X'):
            print_board(board)
            print("You won!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

        computer_move(board)
        if check_winner(board, 'O'):
            print_board(board)
            print("The computer won!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break


if __name__ == "__main__":
    main()