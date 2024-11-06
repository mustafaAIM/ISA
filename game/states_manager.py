from state import GameState
class StateManager:
    def __init__(self):
        self.states = []   

    def save_state(self, board, parent=None, action=None, depth=0, cost=0):
        new_state = GameState(board, parent, action, depth, cost)
        self.states.append(new_state)
        return new_state   

    def get_last_state(self):
        return self.states[-1] if self.states else None

    def clear_states(self):
        self.states.clear()

    def get_state_path(self, end_state):
        return end_state.get_path()
    