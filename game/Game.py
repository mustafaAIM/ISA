from colorama import *
from squirrel import Squirrel
from move_generator import MoveGenerator 

class Game:
    def __init__(self, board, renderer, state_manager):
        self.board = board
        self.renderer = renderer
        self.state_manager = state_manager
        self.current_state = None
        self.move_generator = MoveGenerator(board)

    def play(self): 
        self.current_state = self.state_manager.save_state(
            self.board, parent=None, action=None, depth=0, cost=0
        )

        while True:
            self.renderer.render_board()

            print(Fore.CYAN + " Available pieces:")
            for idx, piece in enumerate(self.board.pieces):
                if isinstance(piece, Squirrel):
                    print(
                        Fore.YELLOW +
                        f"{idx}: {type(piece).__name__} at {piece.positions} with nut at {piece.nut} 🐿️"
                    )
 
            piece_idx = int(input(Fore.GREEN + "🕹️ Choose the piece index to move (or -1 to quit): "))
            if piece_idx == -1:
                print(Fore.RED + "Game exited. 🛑")
                break

            piece = self.board.pieces[piece_idx]
 
            see_moves = input(Fore.GREEN + "👀 Would you like to see possible moves for this piece? (y/n): ").lower()
            if see_moves == 'y':
                possible_states = self.get_possible_moves_for_piece(piece)   
                if possible_states:
                    print(Fore.CYAN + "🔄 Possible moves for the selected piece:")
                    for state in possible_states:
                        direction = state.action[1]   
                        print(Fore.YELLOW + f"➡️ Move direction: {direction}, Depth: {state.depth}")
                else:
                    print(Fore.RED + "❌ No available moves for this piece.")

 
            direction = input(Fore.GREEN + "➡️ Enter direction (UP, DOWN, LEFT, RIGHT): ").upper()
            if direction not in ["UP", "DOWN", "LEFT", "RIGHT"]:
                print(Fore.RED + "❌ Invalid direction! Please choose again.")
                continue
                
            if self.board.can_move(piece, direction):
                self.board.move_piece(piece, direction)
                self.renderer.render_board()
 
                self.current_state = self.state_manager.save_state(
                    board=self.board,
                    parent=self.current_state,
                    action=(piece_idx, direction),
                    depth=self.current_state.depth + 1,
                    cost=self.current_state.cost + 1
                )

                print(Fore.GREEN + "✅ Move successful.")
            else: 
                print(Fore.RED + "❌ Move blocked! Try a different piece or direction.")
 
            if self.board.is_game_end():
                self.renderer.render_board()
                print(Fore.MAGENTA + "🎉 Congratulations! All nuts are in holes. 🏆")
                break

            
            
    def get_possible_moves_for_piece(self, piece):
        current_state = self.state_manager.get_last_state()  
        possible_moves = self.move_generator.generate_possible_moves(piece, current_state)
        
        for move in possible_moves:
            self.state_manager.save_state(
                board=move.board,
                parent=move.parent,
                action=move.action,
                depth=move.depth,
                cost=move.cost
            )

        return possible_moves