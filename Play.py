#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game 
#   

from Board import Board
from Player import Player
from Player import RandomPlayer
from AIPlayer import *
import random




def process_move(player, board):
    '''takes two parameters: a Player object for the player whose move is being
    processed, and a Board object for the game that is being played.
    The function will processe a single move by the specified player on the
    specified board.'''
    print(player, '\'s turn')

    colOfNext_move = player.next_move(board)
    board.add_checker(player.checker, colOfNext_move)
    print()
    print(board)
    if board.is_win_for(player.checker):
        print(player, 'wins in', player.num_moves, 'moves')
        print('Congratulations!')
        return True
    elif board.is_full():
        print('It\'s a tie!')
        return True
    else:
        return False
 
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

if __name__ == "__main__":

    #Getting checker input from user
    player_checker = str(input("What checker would you Prefer X or O ? "))
    player_checker = player_checker.capitalize()
    opp_checker = ''

    try:
        assert(player_checker == 'X' or player_checker== 'O')
    except Exception:
        print("Not a valid Checker!")
        raise
    
    if player_checker == 'X':
        opp_checker += 'O'
    else:
        opp_checker += 'X'

    #Getting difficulty input from user
    difficulty = int(input("What difficult would you prefer 1, 2 or 3 ? "))
    
    
    try:
        assert(difficulty == 1 or difficulty == 2 or difficulty == 3)
    except Exception:
        print("Not a valid difficulty!")
        raise
    
    p1 = Player(player_checker)
    p2 = AIPlayer(opp_checker,'RANDOM', difficulty+1)

    connect_four(p1,p2)


    

