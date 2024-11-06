import copy
from board import Board 
from render import BoardRenderer
from flower import Flower
from squirrel import Squirrel
from squirrelL import SquirrelL
from nut import Nut
from Game import Game
from states_manager import StateManager



def initialize_level(level):
    board = Board(size=(4, 4))   

    if level == 1: 
        flower1 = Flower((1, 0))
        squirrel_L = SquirrelL(positions=[(1, 2), (2, 2), (2, 3)], nut=Nut(2, 2, False))
        squirrel = Squirrel(positions=[(1, 1), (0, 1)], nut=Nut(0,1, False))
        board.add_piece(flower1)
        board.add_piece(squirrel_L)
        board.add_piece(squirrel)

    elif level == 2: 
        flower1 = Flower((2, 1))
        squirrel = Squirrel(positions=[(2, 2), (3, 2)], nut=Nut(2,2, False))
        squirrel_2 = Squirrel(positions=[(1, 1), (1, 2)], nut=Nut(1, 1, False))
        
        board.add_piece(flower1)
        board.add_piece(squirrel)
        board.add_piece(squirrel_2)
    elif level == 3:
        squirrel = Squirrel(positions=[(0,1),(1,1)], nut=Nut(1,1,False))
        squirrel_2 = Squirrel(positions=[(1,2),(1,3)], nut=Nut(1,2,False))
        squirrel_L = SquirrelL(positions=[(2,0),(2,1),(3,1)] , nut = Nut(3,1,False))
        squirrel_L_2 = SquirrelL(positions=[(2,2),(2,3),(3,3)] , nut = Nut(2,3,False))
        
        board.add_piece(squirrel)
        board.add_piece(squirrel_2)
        board.add_piece(squirrel_L)
        board.add_piece(squirrel_L_2)
    return board




def show_possible_moves(game, piece_idx): 
    piece = game.board.pieces[piece_idx]
    possible_moves = game.get_possible_moves_for_piece(piece)
    
    print("\nPossible moves for the selected piece:")
    for move in possible_moves:
        print(f"Move {move.action[1]} to reach depth {move.depth} with cost {move.cost}")
    print("-" * 40)


def main():
    print("Welcome to Squirrels Go Nuts!")
    level = int(input("Choose a level (1-3): "))
 
    board = initialize_level(level)
    renderer = BoardRenderer(board)
    state_manager = StateManager()
    game = Game(board, renderer, state_manager)
    game.play()
    [print(s) for s in game.state_manager.states]

if __name__ == "__main__":
    main()

# end_state = state_manager.get_last_state()  
# path = state_manager.get_state_path(end_state) 
# for state in path:
#     print(f"Action: {state.action}, Depth: {state.depth}, Cost: {state.cost}")


# game.state_manager.save_state(board)
# possibles_states = (game.get_possible_moves_for_piece(squirrel_1x2))
# for state in possibles_states:
#     renderer.board = state.board 
#     renderer.render_board()

# board2 = copy.deepcopy(board)
# print(board == board2)