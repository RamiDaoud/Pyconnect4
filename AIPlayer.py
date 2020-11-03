#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from Player import *

class AIPlayer(Player):
    '''A blueprint for an artificially intelligence Player that
    inherites from Player class'''
    
    def __init__(self,checker,tiebreak,lookahead):
        '''AIPlayer object constructor'''
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM') 
        assert(checker == 'X' or checker == 'O')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead



    def __repr__(self):
        '''returns a string representing an AIPlayer object'''
        s = 'Player ' + self.checker + ' ('+ self.tiebreak + ', '
        s += str(self.lookahead) + ')'
        return s


    def max_score_column(self, scores):
        '''takes a list scores containing a score for each column of
        the board, and that returns the index of the column with
        the maximum score. If one or more columns are tied for
        the maximum score, the method should apply the called
        AIPlayer‘s tiebreaking strategy to break the tie.'''
        list_of_indexs = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                list_of_indexs += [i]
        if self.tiebreak == 'LEFT':
            return list_of_indexs[0]
        elif self.tiebreak == 'RIGHT':
            return list_of_indexs[-1]
        else:
            return random.choice(list_of_indexs)


    def scores_for(self, board):
        '''takes a Board object board and determines the called
        AIPlayer‘s scores for the columns in board.
        return a list containing one score for each column'''
        scores = [7] * board.width
        for col in range(board.width):
            
            if not (board.can_add_to(col)):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker,col)
                AIOpponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                Opponent_scores = AIOpponent.scores_for(board)
                Best_Opponent_score = max(Opponent_scores)
                scores[col] = 100 - Best_Opponent_score
                board.remove_checker(col)

        return scores


    def next_move(self, board):
        '''return the called AIPlayer‘s judgment of its best possible move'''
        scores = self.scores_for(board)
        self.num_moves += 1
        return self.max_score_column(scores)
                
                
            
            
        
                
        
                
                

        

        
        
