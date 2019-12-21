# Tyrone Tong 39813123
'''https://www.youtube.com/watch?v=nsLTQj-l_18'''
import game_mechanics as gm
import pygame
import time

def get_dimensions() -> tuple:
    '''This function gets the dimensions of the board'''
    row = 13
    column = 6
    return (row, column)


def user_input() -> str:
    '''This function is called on when a user input is needed'''
    pressed = False
    time_out = time.time() + 0.2
    while time.time() < time_out :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                return "<"
                pressed = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                return ">"
                pressed = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "R"
                pressed = True
            if event.type == pygame.QUIT:
                quit()
    if pressed == False:
        return ""

def build_board(board_state: list,game_window) -> None:
    '''This function displays the board on the game_window based on the current state of the list inputted'''
    colors = {
        "S": (255,0,0),
        "T": (255,0,0),
        "V": (0,0,255),
        "W": (255,182,193),
        "X": (255,248,220),
        "Y": (170,170,170),
        "Z": (130,130,211),
        " ": (255,255,255),
        "L": (0,0,0)

    }
    empty =[]
    board =[]
    for row in board_state:
        for item in range(len(row)):
            if item == 2 or item ==5 or item ==8 or item ==11 or item ==14 or item ==17:
                empty.append(row[item])
        board.append(empty)
        empty =[]

    for row in range(len(board_state)):
        current_row = board[row]
        for col in range(len(current_row)):
            current_object = current_row[col]
            pygame.draw.rect(game_window,colors[current_object],pygame.Rect(col*(600/6), row*(600/13),100, 600/13))
            pygame.display.flip()

if __name__ == '__main__':
    board = gm.board()
    board.starting_board()
