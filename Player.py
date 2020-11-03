#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class
#

from Board import Board

# write your class below
class Player:
    '''A blueprint for objects of type Player'''



    def __init__(self, checker):
         '''The constructor of the Player object'''
         assert(checker == 'X' or checker == 'O')
         self.checker = checker
         self.num_moves = 0





    def __repr__(self):
        '''returns a string representing a Player object.
        The string returned should indicate which checker the Player object
        is using'''
        s = 'Player ' + self.checker
        return s



    def opponent_checker(self):
        '''returns a one-character string representing the checker
        of the Player object’s opponent.'''

        if self.checker == 'X':
            return 'O'
        return 'X'

    def next_move(self, board):
        '''accepts a Board object as a parameter and returns the
        column where the player wants to make the next move'''

        while True:
            col = int(input('Enter a column:'))
            if board.can_add_to(col):
                self.num_moves += 1
                return col
            else:
                print('Try again!')



class RandomPlayer(Player):
    '''A Blueprint for RandomPlayer Objects that inherits from the Player class'''
    def next_move(self, board):
        '''choose at random from the columns in the specified board that are not
        yet full, and return the index of that randomly selected column'''

        while True:
            col = random.choice(list(range(board.width)))
            if board.can_add_to(col):
                self.num_moves += 1
                return col
        
    
