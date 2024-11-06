import copy
from state import GameState
class MoveGenerator:
    def __init__(self, board):
        self.board = board  

    def generate_possible_moves(self, piece, current_state):
        directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        possible_moves = []

        for direction in directions:
            if current_state.board.can_move(piece, direction):
                new_board = copy.deepcopy(current_state.board)
                new_piece = next(p for p in new_board.pieces if p == piece)  
                new_board.move_piece(new_piece, direction)
                # for pieces in new_board.pieces:
                #     if len(pieces.positions) == 3:
                #         print(pieces.positions)  
                new_state = GameState(
                    board=new_board,
                    parent=current_state,         
                    action=(piece, direction),   
                    depth=current_state.depth + 1,  
                    cost=current_state.cost + 1     
                )

                possible_moves.append(new_state)

        return possible_moves
