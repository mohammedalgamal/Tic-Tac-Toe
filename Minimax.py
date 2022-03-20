"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}
def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    #print board
    m_score = 2
    score = -2
    max_move = (-1, -1)
    min_move = (-1, -1)
    curr1 = (score, max_move)
    curr2 = (m_score, min_move)
    if player == provided.PLAYERX:
        for idx in board.get_empty_squares():
            new_board = board.clone()
            new_board.move(idx[0], idx[1], player)
            if new_board.check_win() != None:
                score = SCORES[new_board.check_win()]
                return score, idx
            move = mm_move(new_board, provided.switch_player(player))          
            if move[0] > curr1[0]:
                curr1 = (move[0], idx)
            score = max(move[0], score)
            if score == 1:
                break
        return score, curr1[1]
    else:
        for idx in board.get_empty_squares():
            new_board = board.clone()
            new_board.move(idx[0], idx[1], player)
            if new_board.check_win() != None:
                m_score = SCORES[new_board.check_win()]
                return m_score, idx
            move = mm_move(new_board, provided.switch_player(player))
            if move[0] < curr2[0]:
                curr2 = (move[0], idx)
            m_score = min(move[0], m_score)
            if m_score == -1:
                break
        return m_score, curr2[1]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
