import copy

class GameState:
    def __init__(self, board, parent=None, action=None, depth=0, cost=0):
        self.board = copy.deepcopy(board)   
        self.parent = parent               
        self.action = action                
        self.depth = depth                  
        self.cost = cost                    

    def __eq__(self, other): 
        return isinstance(other, GameState) and self.board == other.board
 
    def get_path(self):
        path = []
        current_state = self
        while current_state:
            path.append(current_state)
            current_state = current_state.parent
        return path[::-1]  
