"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
from collections import defaultdict


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))

    w, h = game.width / 2., game.height / 2.

    # use distance from location to center
    # x0, y0 = game.get_player_location(player)
    # x1, y1 = game.get_player_location(game.get_opponent(player))
    # own_score = float((10/((h - x0)**2 + (w - y0)**2)))
    # opp_score = float((10/((h - x1)**2 + (w - y1)**2)))

    # use distance of all moves to center
    own_score = sum([float((10/((h - x)**2 + (w - y)**2))) for x,y in own_moves])
    opp_score = sum([float((10/((h - x)**2 + (w - y)**2))) for x,y in opp_moves])

    return float(own_score - opp_score)

    # own_score = float((((h - x0)**2 + (w - y0)**2)))
    # opp_score = float((((h - x1)**2 + (w - y1)**2)))

    # return (opp_score - own_score)

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))

    ## if the move is not at the edge,is good move
    own_good_moves,own_bad_moves = [],[]
    for x,y in own_moves:
        if x % game.height and y % game.width:
            own_good_moves.append((x,y))
        else:
            own_bad_moves.append((x,y))
    
    opp_good_moves,opp_bad_moves = [],[] 
    for x,y in opp_moves:
        if x % game.height and y % game.width:
            opp_good_moves.append((x,y))
        else:
            opp_bad_moves.append((x,y))

    # own_good_moves = [(x,y) for x,y in own_moves if x%6 and y%6 ]
    # own_bad_moves = [(x,y) for x,y in own_moves if not (x%6 and y%6) ]
    # opp_good_moves = [(x,y) for x,y in opp_moves if x%6 and y%6 ]
    # opp_bad_moves = [(x,y) for x,y in opp_moves if not (x%6 and y%6) ]

    return float(1.1*len(own_good_moves) + len(own_bad_moves) - 1.1*len(opp_good_moves) - len(opp_bad_moves))

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = game.get_legal_moves(player)
    own_loc = game.get_player_location(player)

    opp_moves = game.get_legal_moves(game.get_opponent(player))
    opp_loc = game.get_player_location(game.get_opponent(player))

    directions = {(-1,-2):'left_top',(-2,-1):'left_top',(-2,1):'right_top',(-1,2):'right_top',\
                  (1,-2):'left_down',(2,-1):'left_down',(2,1):'right_down',(1,2):'right_down'}

    own_move_directions = len(set([directions[(x - own_loc[0],y - own_loc[1])] for x,y in own_moves]))
    opp_move_direcitons = len(set([directions[(x - opp_loc[0],y - opp_loc[1])] for x,y in opp_moves]))

    own_coef = own_move_directions/(own_move_directions+opp_move_direcitons)
    opp_coef = opp_move_direcitons/(own_move_directions+opp_move_direcitons)

    return float(own_coef*len(own_moves) - opp_coef*len(opp_moves))

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            return self.minimax(game, self.search_depth)
            # return self.minimax_all(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    # ref:https://en.wikipedia.org/wiki/Minimax
    def minimax_all(self, game, depth,is_max_player = True):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        if not legal_moves or depth < 1:
            return self.score(game,game.active_player)
        
        # if game.active_player == self:
        # use this condition can also know who is max_palyer
        if is_max_player :
            best_v = float("-inf")
            for m in legal_moves:
                v = self.minimax_all(game,depth-1,False)
                best_v = max(best_v,v)
            return best_v
        else:
            best_v = float("inf")
            for m in legal_moves:
                v = self.minimax_all(game,depth-1,True)
                best_v = min(best_v,v)
            return best_v

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        # raise NotImplementedError

        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1,-1)

        _, move = max([(self.min_value(game.forecast_move(m),depth-1), m) for m in legal_moves])

        # result = []
        # for m in legal_moves:
        #     result.append((self.min_value(game.forecast_move(m),depth-1),m))
        # v, move = max(result) 

        # print(move)
        return move

    def max_value(self,game,depth):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()
        if not moves or depth < 1:
            return self.score(game,game.active_player)

        v = float("-inf")

        for m in moves:
            v = max(v,self.min_value(game.forecast_move(m),depth-1))
        
        # print("max value:{},depth:{}".format(v,depth))
        return v

    def min_value(self,game,depth):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()
        if not moves or depth < 1:
            return self.score(game,game.inactive_player)

        v = float("inf")

        for m in moves:
            v = min(v,self.max_value(game.forecast_move(m),depth-1))
        # print("min value:{},depth:{}".format(v,depth))
        return v


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            depth = 1
            while depth > 0:
                
                move = self.alphabeta(game,depth)
                if move is None:
                    continue

                best_move = move
                best_score = self.score(game.forecast_move(best_move),game.active_player)
                if best_score == float('inf'):
                    break

                depth += 1

            # return self.alphabeta(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        # raise NotImplementedError

        moves = game.get_legal_moves()
        if not moves:
            return (-1,-1)

        best_v = float("-inf")
        move = None
        for m in moves:
            v = self.min_value(game.forecast_move(m),depth-1,best_v,beta)
            if v > best_v:
                best_v = v
                move = m

        return move

        # result = defaultdict(list)
        # for m in legal_moves:
        #     v = self.min_value(game.forecast_move(m),depth-1,alpha,beta)
        #     result[v].append(m)
        # _,moves = max((v,m) for v,m in result.items())

        # return sorted(moves)[0]

    def max_value(self,game,depth,alpha,beta):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()
        if not moves or depth < 1:
            return self.score(game,game.active_player)

        # order_moves = sorted([(self.score(game.forecast_move(m),game.active_player),m) for m in sorted(moves)],reverse=True)

        v = float("-inf")

        # for _,m in order_moves:
        for m in moves:
            v = max(v,self.min_value(game.forecast_move(m),depth-1,alpha,beta))
            if v >= beta:
                return v
            alpha = max(alpha,v)

        return v

    def min_value(self,game,depth,alpha,beta):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        moves = game.get_legal_moves()
        if not moves or depth < 1:
            return self.score(game,game.inactive_player)

        # order_moves = sorted([(self.score(game.forecast_move(m),game.inactive_player),m) for m in sorted(moves)],reverse=False)
        v = float("inf")
        # for _,m in order_moves:
        for m in moves:
            v = min(v,self.max_value(game.forecast_move(m),depth-1,alpha,beta))
            if v <= alpha:
                return v
            beta = min(beta,v)

        return v

