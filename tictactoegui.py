import PySimpleGUI as sg
import random
import numpy as np


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
    b_size = (6, 3)

    layout = [
        [
            sg.Text(
                "Tic Tac Toe", font=("Courier New", "14"), key="text", expand_x=True
            ),
            sg.Button(
                "Reset",
                size=(6, 1),
                key="reset",
                font=("Courier New", "10"),
                button_color=(None, "#585858"),
            ),
        ],
        [
            sg.Button(size=b_size, key="1"),
            sg.Button(size=b_size, key="2"),
            sg.Button(size=b_size, key="3"),
        ],
        [
            sg.Button(size=b_size, key="4"),
            sg.Button(size=b_size, key="5"),
            sg.Button(size=b_size, key="6"),
        ],
        [
            sg.Button(size=b_size, key="7"),
            sg.Button(size=b_size, key="8"),
            sg.Button(size=b_size, key="9"),
        ],
    ]

    window = sg.Window("Tic Tac Toe", layout, finalize=True)

    turns = random.choice(
        [
            ["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"],
        ]
    )

    game = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

    buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    i = 0

    while True:
        turn = turns[i]

        if turn == "X" or checkWin(game) == "X":
            color = "red"
        elif turn == "O" or checkWin(game) == "O":
            color = "blue"

        if "win" in buttons:
            window["text"].update(f"{checkWin(game)} Wins", text_color="green")
        elif "tie" in buttons:
            window["text"].update("Its a tie!", text_color="white")
        else:
            window["text"].update(f"{turn}'s turn", text_color=color)

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event in buttons:
            window[event].update(turn, button_color=(color, "yellow"))

            buttons.remove(event)

            i += 1

            row_index = (int(event) - 1) // 3
            col_index = (int(event) - 1) % 3
            game[row_index][col_index] = turn

            if checkWin(game) in ["X", "O"]:
                window["reset"].update(button_color="red")
                buttons = ["win"]

            continue

        if i >= 8:
            window["reset"].update(button_color="red")
            buttons = ["tie"]

        if event == "reset":
            break
    break

    window.close()
