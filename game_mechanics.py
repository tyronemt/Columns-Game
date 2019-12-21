# Tyrone Tong 39813123
import project5 as game
import copy
import random
import pygame

class board:
    def starting_board(self) -> None:
        ''' This function creates the list if it is empty or has contents in it'''
        user_input_lst = []
        lst = []
        built_row = []
        contents_lst = []
        dimensions = game.get_dimensions()
        row = dimensions[0]
        column = dimensions[1]
        for i in range(row):
            built_row.append('|')
            for x in range(column * 3):
                built_row.append(" ")
            built_row.append('|')
            lst.append(built_row)
            built_row = []
        self.fall(lst)


    def fall(self,board_state) -> None:
        '''This function is called on when a user puts in a command that starts with F its purpose is to iterate throught the rows and make changes to the function'''
        pygame.init()
        game_window = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Columns")
        game_window.fill((255,255,255))
        pygame.display.flip()
        gameExit = False
        game.build_board(board_state,game_window)
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    quit()
            color = ["S", "T", "V", "W", "X", "Y", "Z"]
            colors = [color[random.randint(0, 6)], color[random.randint(0, 6)], color[random.randint(0, 6)]]
            copy_board_state = copy.deepcopy(board_state)
            interesting_column = (random.randint(1,6) * 3) - 1
            for rows_index in range(len(board_state)):
                x = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors, game_window)
                if x[0] == "NEW":
                    board_state = x[1]
                    break
                elif x[0] == "True":
                    interesting_column = x[1]
                elif x[0] == "SIDE":
                    interesting_column = x[1]
                elif x[0] == "ROTATE":
                    colors = x[1]
                else:
                    self.game_over()
                    quit()
            board_state = self.check_board(board_state,game_window)

    def straight(self, board_state: list, rows_index: int, interesting_column: int, copy_board_state: list,colors: list,game_window) -> bool:
        '''This function makes changes to the board as it iterates through the rows where it is called on'''
        indexes = 2
        if rows_index == 0:
            current_row = board_state[rows_index]
            if current_row[interesting_column] == " ":
                current_row[interesting_column - 1] = '['
                current_row[interesting_column + 1] = ']'
                current_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    return ("True", interesting_column)
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("ROTATE", colors)

            else:
                game.build_board(board_state,game_window)
                return "False"

        if rows_index == 1:
            previous_row = board_state[rows_index - 1]
            current_row = board_state[rows_index]
            if current_row[interesting_column] == " ":
                previous_row[interesting_column - 1] = '['
                previous_row[interesting_column + 1] = ']'
                current_row[interesting_column - 1] = '['
                current_row[interesting_column + 1] = ']'
                previous_row[interesting_column] = colors[indexes - 1]
                current_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    return ("True", interesting_column)
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("ROTATE", colors)

            else:
                previous_row[interesting_column - 1] = '|'
                previous_row[interesting_column + 1] = '|'
                previous_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    game.build_board(board_state,game_window)
                    return "False"
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("ROTATE", colors)

        if rows_index == 2:
            previous_row2 = board_state[rows_index - 2]
            previous_row = board_state[rows_index - 1]
            current_row = board_state[rows_index]
            if current_row[interesting_column] == " ":
                previous_row2[interesting_column - 1] = '['
                previous_row2[interesting_column + 1] = ']'
                previous_row[interesting_column - 1] = '['
                previous_row[interesting_column + 1] = ']'
                current_row[interesting_column - 1] = '['
                current_row[interesting_column + 1] = ']'
                previous_row2[interesting_column] = colors[indexes - 2]
                previous_row[interesting_column] = colors[indexes - 1]
                current_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    return ("True", interesting_column)
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    previous_row2[interesting_column] = ' '
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("ROTATE", colors)

            else:
                previous_row2[interesting_column - 1] = '|'
                previous_row2[interesting_column + 1] = '|'
                previous_row[interesting_column - 1] = '|'
                previous_row[interesting_column + 1] = '|'
                previous_row2[interesting_column] = colors[indexes - 1]
                previous_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    game.build_board(board_state,game_window)
                    return "False"
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3]:
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    previous_row2[interesting_column] = ' '
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("ROTATE", colors)

        if rows_index > 2 and rows_index != len(board_state) - 1:
            previous_row2 = board_state[rows_index - 2]
            previous_row = board_state[rows_index - 1]
            current_row = board_state[rows_index]
            if current_row[interesting_column] == " ":
                previous_row2[interesting_column - 1] = '['
                previous_row2[interesting_column + 1] = ']'
                previous_row[interesting_column - 1] = '['
                previous_row[interesting_column + 1] = ']'
                current_row[interesting_column - 1] = '['
                current_row[interesting_column + 1] = ']'
                board_state[rows_index - 3] = copy_board_state[rows_index - 3]
                previous_row2[interesting_column] = colors[indexes - 2]
                previous_row[interesting_column] = colors[indexes - 1]
                current_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    return ("True", interesting_column)
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    previous_row2[interesting_column] = ' '
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("ROTATE", colors)
            else:
                rows_index = rows_index - 1
                previous_row2 = board_state[rows_index - 2]
                previous_row = board_state[rows_index - 1]
                current_row = board_state[rows_index]
                current_row[interesting_column - 1] = '|'
                current_row[interesting_column + 1] = '|'
                previous_row2[interesting_column - 1] = '|'
                previous_row2[interesting_column + 1] = '|'
                previous_row[interesting_column - 1] = '|'
                previous_row[interesting_column + 1] = '|'
                board_state[rows_index - 3] = copy_board_state[rows_index - 3]
                previous_row2[interesting_column] = colors[indexes - 2]
                previous_row[interesting_column] = colors[indexes - 1]
                current_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    return ("NEW", board_state)
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("SIDE", interesting_column)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    previous_row2[interesting_column] = ' '
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("ROTATE", colors)

        if (rows_index + 1) == len(board_state):
            previous_row2 = board_state[rows_index - 2]
            previous_row = board_state[rows_index - 1]
            current_row = board_state[rows_index]
            if current_row[interesting_column] == " ":
                previous_row2[interesting_column - 1] = '|'
                previous_row2[interesting_column + 1] = '|'
                previous_row[interesting_column - 1] = '|'
                previous_row[interesting_column + 1] = '|'
                current_row[interesting_column - 1] = '|'
                current_row[interesting_column + 1] = '|'
                board_state[rows_index - 3] = copy_board_state[rows_index - 3]
                previous_row2[interesting_column] = colors[indexes - 2]
                previous_row[interesting_column] = colors[indexes - 1]
                current_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    previous_row2[interesting_column] = colors[indexes - 2]
                    previous_row[interesting_column] = colors[indexes - 1]
                    current_row[interesting_column] = colors[indexes]
                    return ("NEW", board_state)
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return (y[0], y[1])
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return (y[0], y[1])
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    previous_row2[interesting_column] = ' '
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("NEW", board_state)
            else:
                rows_index = rows_index - 1
                previous_row2 = board_state[rows_index - 2]
                previous_row = board_state[rows_index - 1]
                current_row = board_state[rows_index]
                current_row[interesting_column - 1] = '|'
                current_row[interesting_column + 1] = '|'
                previous_row2[interesting_column - 1] = '|'
                previous_row2[interesting_column + 1] = '|'
                previous_row[interesting_column - 1] = '|'
                previous_row[interesting_column + 1] = '|'
                board_state[rows_index - 3] = copy_board_state[rows_index - 3]
                previous_row2[interesting_column] = colors[indexes - 2]
                previous_row[interesting_column] = colors[indexes - 1]
                current_row[interesting_column] = colors[indexes]
                game.build_board(board_state,game_window)
                user_input = game.user_input()
                if user_input == "":
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    return ("NEW")
                elif user_input == "<":
                    if current_row[interesting_column - 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column - 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("NEW", board_state)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == ">":
                    if current_row[interesting_column + 3] == ' ':
                        previous_row2[interesting_column - 1] = ' '
                        previous_row2[interesting_column + 1] = ' '
                        previous_row2[interesting_column] = ' '
                        previous_row[interesting_column - 1] = ' '
                        previous_row[interesting_column + 1] = ' '
                        previous_row[interesting_column] = " "
                        current_row[interesting_column - 1] = ' '
                        current_row[interesting_column + 1] = ' '
                        current_row[interesting_column] = ' '
                        interesting_column = interesting_column + 3
                        board_state = copy.deepcopy(copy_board_state)
                        y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        interesting_column = y[1]
                        return ("NEW", board_state)
                    else:
                        board_state = copy.deepcopy(copy_board_state)
                        self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                        return ("SIDE", interesting_column)
                elif user_input == "R":
                    previous_row2[interesting_column - 1] = ' '
                    previous_row2[interesting_column + 1] = ' '
                    previous_row2[interesting_column] = ' '
                    previous_row[interesting_column - 1] = ' '
                    previous_row[interesting_column + 1] = ' '
                    previous_row[interesting_column] = " "
                    current_row[interesting_column - 1] = ' '
                    current_row[interesting_column + 1] = ' '
                    current_row[interesting_column] = ' '
                    last_element = colors[2]
                    colors.pop(2)
                    colors = [last_element] + colors
                    y = self.straight(board_state, rows_index, interesting_column, copy_board_state, colors,game_window)
                    if type(y[1]) == int:
                        pass
                    else:
                        colors = y[1]
                    return ("NEW", board_state)

    def check_board(self, board_state: list,game_window) -> list:
        ''' This function is called on after every new move to check if the board has any 3 or more in a row. It takes
        in the current board and returns the modified board'''
        x = self.vertical(board_state)
        y = self.horizontal(board_state)
        z = self.diagonal(board_state)
        t = board_state
        if x == False or y == False or z == False:
            game.build_board(board_state,game_window)
            user_input = game.user_input()
            if user_input == "":
                self.clear_board(board_state)
                t = self.clean_board(board_state)
                game.build_board(t,game_window)
            else:
                game.build_board(board_state,game_window)
                self.game_over()
        else:
            game.build_board(board_state,game_window)
        return t

    def vertical(self, board_state: list) -> bool:
        '''This function is the first step of the check board function. It take in the current board and checks if there
        is any three or more in a row vertically and put stars around the indicated region and then returns whether the board was motified'''
        copy_board_state = copy.deepcopy(board_state)
        for rows_index in range(len(board_state)):
            if rows_index == 0:
                pass
            elif rows_index < len(board_state) - 1:
                previous_row = board_state[rows_index - 1]
                current_row = board_state[rows_index]
                future_row = board_state[rows_index + 1]
                for index in range(len(current_row)):
                    if current_row[index] != " " and current_row[index] != '*' and current_row[index] != '|':
                        if previous_row[index] == current_row[index] and current_row[index] == future_row[index]:
                            previous_row[index + 1] = "*"
                            previous_row[index] ="L"
                            current_row[index + 1] = "*"
                            current_fow[index] = "L"
                            future_row[index + 1] = "*"
                            future_row[index] = "L"
                            previous_row[index - 1] = "*"
                            current_row[index - 1] = "*"
                            future_row[index - 1] = "*"
            elif rows_index == (len(board_state) - 1):
                previous_row2 = board_state[rows_index - 2]
                previous_row = board_state[rows_index - 1]
                current_row = board_state[rows_index]
                for index in range(len(current_row)):
                    if current_row[index] != " " and current_row[index] != '*' and current_row[index] != '|':
                        if previous_row[index] == current_row[index] and current_row[index] == previous_row2[index]:
                            previous_row[index + 1] = "*"
                            current_row[index + 1] = "*"
                            previous_row2[index + 1] = "*"
                            previous_row[index - 1] = "*"
                            current_row[index - 1] = "*"
                            previous_row2[index - 1] = "*"
                            previous_row[index] = "L"
                            current_fow[index] = "L"
                            future_row[index] = "L"
        return board_state == copy_board_state

    def horizontal(self, board_state: list) -> bool:
        '''This function is the second step of the check board function. It take in the current board and checks if there
        is any three or more in a row horizantally and put stars around the indicated region and then returns whether the board was motified'''
        copy_board_state = copy.deepcopy(board_state)
        for rows_index in range(len(board_state)):
            current_row = board_state[rows_index]
            for index in range(len(current_row)):
                if current_row[index] != " " and current_row[index] != '*' and current_row[
                    index] != '|' and index != 2 and index != (len(current_row) - 3):
                    if current_row[index] == current_row[index - 3] and current_row[index] == current_row[index + 3]:
                        current_row[index + 2] = "*"
                        current_row[index] = "L"
                        current_row[index + 1] = "*"
                        current_row[index + 4] = "*"
                        current_row[index - 3] = "L"
                        current_row[index - 2] = "*"
                        current_row[index - 1] = "*"
                        current_row[index + 3] = "L"
                        current_row[index - 4] = "*"
        return board_state == copy_board_state

    def diagonal(self, board_state: list) -> bool:
        '''This function is the last step of the check board function. It take in the current board and checks if there
        is any three or more in a row diagonally in both directions and put stars around the indicated region
        and then returns whether the board was motified'''
        copy_board_state = copy.deepcopy(board_state)
        for rows_index in range(len(board_state)):
            try:
                previous_row = board_state[rows_index - 1]
                current_row = board_state[rows_index]
                future_row = board_state[rows_index + 1]
                if rows_index == 0:
                    pass
                elif rows_index < len(board_state) - 1:
                    previous_row = board_state[rows_index - 1]
                    current_row = board_state[rows_index]
                    future_row = board_state[rows_index + 1]
                for index in range(len(current_row)):
                    if current_row[index] != " " and current_row[index] != '*' and current_row[
                        index] != '|' and index != 2 and index != (len(current_row) - 3):
                        if current_row[index] == previous_row[index - 3] and current_row[index] == future_row[
                            index + 3]:
                            previous_row[index - 3 + 1] = "*"
                            previous_row[index - 3] ="L"
                            current_row[index + 1] = "*"
                            future_row[index + 1 + 3] = "*"
                            future_row[index + 3] ="L"
                            previous_row[index - 3 - 1] = "*"
                            current_row[index - 1] = "*"
                            current_row[index] = "L"
                            future_row[index - 1 + 3] = "*"
                        elif current_row[index] == future_row[index - 3] and current_row[index] == previous_row[
                            index + 3]:
                            future_row[index + 1 - 3] = "*"
                            future_row[index - 3] = "L"
                            current_row[index + 1] = "*"
                            current[row_index] ="L"
                            previous_row[index + 1 + 3] = "*"
                            future_row[index - 1 - 3] = "*"
                            previous_row[index + 3] ="L"
                            current_row[index - 1] = "*"
                            previous_row[index - 1 + 3] = "*"
            except IndexError:
                pass
        return board_state == copy_board_state

    def clear_board(self, board_state: list) -> None:
        '''This function is called on if the current board was modified and turns all colors indicated with stars to blank spaces'''
        for rows_index in range(len(board_state)):
            current_row = board_state[rows_index]
            for item in range(int(((len(current_row)) - 2) / 3)):
                item = (((item + 1) * 3) - 1)
                if current_row[item - 1] == '*' and current_row[item + 1] == '*':
                    current_row[item - 1] = ' '
                    current_row[item + 1] = ' '
                    current_row[item] = ' '

    def clean_board(self, board_state: list) -> list:
        '''This function is called to make the floating colors drop to the bottom so there are no blank spaces and then returns the current board'''
        built_row = []
        temp_lst = []
        column_lst = []
        final_lst = []
        len_row = board_state[0]
        for i in range(len(len_row)):
            for rows in board_state:
                built_row.append(rows[i])
            temp_lst.append(built_row)
            built_row = []
        for content in temp_lst:
            for x in range(len(content)):
                if content[x] == " ":
                    content.pop(x)
                    content.insert(0, " ")
            column_lst.append(content)
        len_col = column_lst[0]
        for i in range(len(len_col)):
            for column in column_lst:
                built_row.append(column[i])
            final_lst.append(built_row)
            built_row = []
        return final_lst

    def game_over(self) -> None:
        '''This function is called on whenever the games rule is broken resulting in a Game Over'''
        print("GAME OVER")
