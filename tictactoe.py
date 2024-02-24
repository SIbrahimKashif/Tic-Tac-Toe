import numpy as np
import random

print("\n---Tic Tac Toe: 2 Player---\n")

player1 = input("Player 1 (X): ").title().strip()
player2 = input("Player 2 (O): ").title().strip()


# check for wins
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0


def checkDiagonals(board):
    if len(set([board[j][j] for j in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[j][len(board) - j - 1] for j in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return 0


def checkWin(board):
    # transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


while True:
    i = 0

    board = f"""\n1 | 2 | 3 \n--|---|--\n4 | 5 | 6 \n--|---|--\n7 | 8 | 9 \n"""
    grid = board

    game = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

    turns = random.choice(
        [
            ["X", "O", "X", "O", "X", "O", "X", "O", "X"],
            ["O", "X", "O", "X", "O", "X", "O", "X", "O"],
        ]
    )

    print(grid)

    if len(player1) == 0:
        player1 = "X"
    if len(player2) == 0:
        player2 = "O"

    while True:
        # check for win
        if checkWin(game) in ["X", "O"]:
            if checkWin(game) == "X":
                won = player1
            elif checkWin(game) == "O":
                won = player2

            print(f"'{won}' Wins!\n")
            break

        # check for draw
        elif i == 9:
            # print("\n---Game Over---\n")
            print("Its a tie!")
            break

        turn = turns[i]

        if turn == "X":
            player = player1
        else:
            player = player2

        num = input(f"{player}'s turn ({turn}) : ")

        if num.isnumeric():
            if str(num) in board:
                board = board.replace(num, turn)

                new_board = board

                for n in range(1, 10):
                    if str(n) in new_board:
                        new_board = new_board.replace(str(n), " ")
                print(board)

                row_index = (int(num) - 1) // 3
                col_index = (int(num) - 1) % 3
                game[row_index][col_index] = turn

                i = i + 1
                continue
            else:
                print("\nPosition is already occupied")
        else:
            print("\nPlease enter a number from the board\n")
            continue

    quit = input("Press enter to play again or press q to quit: ")
    print()
    if quit == "q":
        break
    else:
        continue
