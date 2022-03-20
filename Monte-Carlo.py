"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    The function should play a game starting with the given player by making random moves, 
    alternating between players. 
    The function should return when the game is over.
    """
    while board.check_win() == None:
        chose = random.choice(board.get_empty_squares())
        row = chose[0]
        col = chose[1]
        board.move(row, col, player)
        player = provided.switch_player(player)
    return

def mc_update_scores(scores, board, player):
    """
     This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, 
     a board from a completed game,
     and which player the machine player is. 
     The function should score the completed board and update the scores grid.
     """
    if board.check_win() == player:
        win_cur = 1
        win_oth = -1
    elif board.check_win() == provided.switch_player(player):
        win_cur = -1
        win_oth = 1
    else:
        win_cur = 0
        win_oth = 0
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) == player:
                scores[row][col] += (SCORE_CURRENT * win_cur)   
            elif board.square(row, col) == provided.switch_player(player):
                scores[row][col] += (SCORE_OTHER * win_oth)
            else:
                scores[row][col] += 0        
    
def get_best_move(board, scores):
    """
     This function takes a current board and a grid of scores. 
     The function should find all of the empty squares with the maximum score 
     and randomly return one of them
     """
    if len(board.get_empty_squares()) > 1:
        max_score = -100000
        max_move = 0
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if scores[row][col] >= max_score and board.square(row, col) == provided.EMPTY:
                    max_score = scores[row][col]
                    max_move = (row, col)                    
        return max_move
    else:
        max_move = board.get_empty_squares()[0]
        return max_move
    
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, 
    and the number of trials to run. The function should use the Monte Carlo simulation described above 
    to return a move for the machine player
    """
    if board.get_empty_squares() != []:
        ins_list = list([0]) * (board.get_dim())
        scores = [list(ins_list)]
        for dummy in range(board.get_dim() - 1):
            scores += [list(ins_list)]   
        for dummy in range(trials):
            #scores = [[0] * (board.get_dim())] * (board.get_dim())
            current_board = board.clone()
            mc_trial(current_board, player)
            mc_update_scores(scores, current_board, player)
        move = get_best_move(board, scores)      
        return move
    else:
        return

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
