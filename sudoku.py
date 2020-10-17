import sys
sys.setrecursionlimit(20000)

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 0, 0, 4, 0, 2, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 0, 2, 0, 6, 0, 0, 7]
]


def show_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("-" * ((len(board[0]) * 2) + 3))
            for j in range(len(board[0])):
                if j == len(board[0]) - 1:
                    print(board[i][j], end="|\n")
                else:
                    if j % 3 == 0:
                        print("|", end="")

                    print(str(board[i][j]) + " ", end="")
        else:
            for j in range(len(board[0])):
                if j == len(board[0]) - 1:
                    print(board[i][j], end="|\n")
                else:
                    if j % 3 == 0:
                        print("|", end="")

                    print(str(board[i][j]) + " ", end="")
    print("-" * ((len(board[0]) * 2) + 3))


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if is_empty(board, i, j):
                return i, j
    return None


def is_empty(board, i, j):
    return board[i][j] == 0


def check_row(board, number, position):
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    return True


def check_column(board, number, position):
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    return True


def check_box(board, number, position):
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def is_valid(board, number, position):
    return (check_row(board, number, position) and
            check_column(board, number, position) and
            check_box(board, number, position))


def solve(board):

    empty = find_empty(board)

    if not empty:
        return True
    else:
        row, column = empty

    for i in range(1, 10):
        if is_valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True

            board[row][column] = 0

    return False


if __name__ == "__main__":
    show_board(board)
    solve(board)
    show_board(board)
