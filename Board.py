#
# ps10pr1.py - Problem Set 10, Problem 1
#
# A Connect Four Board class
#

# 
class Board:
    ''' A blueprint for objects of type Board'''
    def __init__(self, height, width):
        '''the constructor of the object'''
        self.height = height
        self.width  = width
        self.slots = [ [' ']*self.width for x in range(self.height) ]

    def __repr__(self):
        '''returns a string representing a Board object'''

        s = ''

        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col]
                s += '|'
            s += '\n'

        for col in range(self.width):
            s += '--'
        s += '-'
        s += '\n'
        for col in range(self.width):
            s += ' ' + str(col % 10)

        return s

    def add_checker(self, checker, col):
        '''takes two input:
        checker, a one-character string that specifies the checker
        to add to the board (either 'X' or 'O').
        col, an integer that specifies the index of the column to
        which the checkershould be added and that adds checker to
        the appropriate row in column col of the board.'''

        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = -1
        while (row + 1 < self.height) and (self.slots[row + 1][col] == ' ') :
            row += 1
        if row != -1 :
            self.slots[row][col] = checker


    def reset(self):
        '''reset the Board object on which it is called by setting
        all slots to contain a space character'''

        for col in range(self.width):
            row = 0
            while row - 1 >= - self.height and  -row - 1 != ' ':
                row = row - 1
                self.slots[row][col] = ' '


    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object,
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)

            if (0 <= col < self.width):
                self.add_checker(checker, col)

        # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'



    def can_add_to(self, col):
        '''returns True if it is valid to place a checker in the column
        col on the calling Board object. Otherwise, it should return False.'''

        if  0 <= col < self.width and self.slots[0][col] == ' ':
            return True
        return False



    def is_full(self):
        '''returns True if the called Board object is completely full
        of checkers, and returns False otherwise.'''

        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True


    def remove_checker(self, col):
        '''removes the top checker from column col of the called Board object.
        If the column is empty, then the method should do nothing'''
        if self.slots[-1][col] != ' ':
            row = 0
            while row + 1 < self.height:
                if self.slots[row][col] != ' ':
                    break
                row += 1
            self.slots[row][col] = ' '


    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False



    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for col in range(self.width):
            for row in range(self.height -3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    def is_down_diagonal_win (self, checker):
        """ Checks for a diagonal down from left to right win for the specified checker.
        """
        for col in range(self.width - 3):
            for row in range(self.height -3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    def is_up_diagonal_win (self, checker):
        """ Checks for a diagonal up from left to right win for the specified checker.
        """
        for col in range(self.width - 3):
            for row in range(3,self.height):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False



    def is_win_for(self, checker):
        '''accepts a parameter checker that is either 'X' or 'O',
        and returns True if there are four consecutive slots
        containing checker on the board.
        Otherwise, it should return False.'''

        assert(checker == 'X' or checker == 'O')

        result = self.is_up_diagonal_win(checker) or self.is_down_diagonal_win(checker) or self.is_horizontal_win(checker) or self.is_vertical_win(checker)
        return result
