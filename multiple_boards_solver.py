#  TODO - add comments!!!

import sys
import csv 
from datetime import datetime
import time
from statistics import mean

FILENAME = sys.argv[1]
NUM_LINES_BOARD = 9

def main():
    start_time = time.time()
    print(datetime.now().time(), "\n\n")
    boards, bool_boards = get_boards_from_file(FILENAME)
    assert len(boards) == len(bool_boards)
    # for every board in our file, let's solve it
    for i in range(len(boards)):
        board_time = time.time()
        # start analyzing board at 0,0
        row = 0
        col = 0
        # start program by looking for first open cell
        if (bool_boards[i][row][col] != True):
            while True:
                # print("looking for next cell...")
                if col == 8 and row == 8: # then the end of the board has been reached
                    bprint(boards[i])
                    print("Board is already solved!")
                    return
                col += 1
                if col == 9: # in case I exceed the range of the board
                    col = 0
                    row +=1 # when I reset col to be 0, I also move one row down
                    if row == 9:
                        bprint(boards[i])
                        print("Board is already solved!")
                        return
                if bool_boards[i][row][col] == True:
                    break
        print(i)
        # start program by analyzing cell (0,0)
        print(row,col)
        solve_cell(boards[i], bool_boards[i], row, col)
        partial_time = time.time() - board_time
        print("Time: {}".format(partial_time))
    print("Program terminated! Total runtime: {}".format(time.time() - start_time))

def is_valid(board, guess, row, col):
    cell_value = board[row][col]
    row_neighs = get_row_elems(board, row, cell_value)
    col_neighs = get_col_elems(board, col, cell_value)
    box_neighs = get_box_elems(board, row, col, cell_value)

    if guess not in row_neighs and guess not in col_neighs and guess not in box_neighs:
        return True
    else:
        return False

def bprint(board):
    assert type(board) is list
    for line in board:
        print (line)
    print ("\n")

def solve_cell(board, bool_board, row, col):
    for i in range(1,10):
        if is_valid(board, i, row, col):
            # track old values
            old_row = row
            old_col = col
            # set the value of that cell to be i
            board[row][col] = i
            # this code for finding the next open cell works well
            # move on to solve the next cell
            while True:
               # print("looking for next cell...")
                if col == 8 and row == 8: # then the end of the board has been reached
                    bprint(board)
                    return
                col += 1
                if col == 9: # in case I exceed the range of the board
                    col = 0
                    row +=1 # when I reset col to be 0, I also move one row down
                    if row == 9:
                        bprint(board)
                        return
                if bool_board[row][col] == True:
                    break
            # if the while loop is exited, then it means a row col pair was found such that
            # that spot on the board was available for user input
            # RECURSE
           # print("recursing, exploring new cell", row, col)
            #bprint(board)
            solve_cell(board, bool_board, row, col)
            # if the recursion comes back, then it means it's backtracking, so we need to undo all the changes
           # print("reset", row , col)
            board[row][col] = 0
            row = old_row
            col = old_col
            #bprint(board)

def get_row_elems(board, row, cell_value):
    # this function aims to retrieve all the numbers on the same row as the scrutinized cell
    neighs = []
    for value in board[row]:
        if value == 0 or value == cell_value:
            continue
        neighs.append(value)
    return neighs

def get_col_elems(board, col, cell_value):
    neighs = []
    for row in range(len(board)):
        if board[row][col] == 0 or board[row][col] == cell_value:
            continue
        neighs.append(board[row][col])  
    return neighs

def get_box_elems(board, row, col, cell_value):
    box_start_x = int(row/3)*3
    box_start_y = int(col/3)*3
    box = fetch_box_from_board(board, box_start_x, box_start_y)
    if cell_value in box:
        box.remove(cell_value)
    return box 

def fetch_box_from_board(board, x,y):
    box = []
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] != 0:
                box.append(board[i][j])
    return box


def get_boards_from_file(FILENAME):
    list_matrix = []
    list_bool_matrix = []
    with open (FILENAME, "r") as csvfile:
        boardcsv = csv.reader(csvfile)
        matrix = []
        bool_matrix = []
        counter = 0
        for line in boardcsv:
            counter += 1
            if counter > NUM_LINES_BOARD:
                counter = 0
                list_matrix.append(matrix)
                matrix = []
                list_bool_matrix.append(bool_matrix)
                bool_matrix = []
                continue
            line = [int(item) if item.isdigit() else item for item in line]
            matrix.append(line)
            bool_line = []
            for elem in line:
                if elem == 0:
                    bool_line.append(True)
                else:
                    bool_line.append(False)
            bool_matrix.append(bool_line)     
    return list_matrix, list_bool_matrix


if __name__ == "__main__":
    main()
