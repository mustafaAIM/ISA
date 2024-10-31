from colorama import *
init(autoreset=True) 
class BoardRenderer:
    def __init__(self, board):
        self.board = board
        self.symbols = {
            'HOLE_FILLED': "🕳️",
            'HOLE_EMPTY': "⚪",
            'SQUIRREL_WITH_NUT': "🐿️",
            'FLOWER': "🌼",
            'NUT': "🌰",
            'GRASS': "🍃",
        }

    def render_board(self):
        size = self.board.size
        pieces = self.board.pieces
        holes = self.board.holes

        # Initialize empty board
        board_repr = [["  " for _ in range(size[1])] for _ in range(size[0])]

        # Place holes on the board
        for hole in holes:
            symbol = self.symbols['HOLE_FILLED'] if hole.status else self.symbols['HOLE_EMPTY']
            board_repr[hole.x][hole.y] = symbol

        # Place each piece on the board
        for piece in pieces:
            if isinstance(piece, SquirrelL):
                self._render_squirrelL(board_repr, piece)
            elif isinstance(piece, Squirrel):
                self._render_squirrel(board_repr, piece)
            elif isinstance(piece, Flower):
                self._render_flower(board_repr, piece)

        # Output board to console
        self._display_board(board_repr)

    def _render_squirrelL(self, board_repr, piece):
        for (x, y) in piece.positions:
            board_repr[x][y] = self.symbols['NUT'] if (x, y) == (piece.nut.x, piece.nut.y) and not piece.nut.status else self.symbols['GRASS']

    def _render_squirrel(self, board_repr, piece):
        for (x, y) in piece.positions:
            board_repr[x][y] = self.symbols['NUT'] if (x, y) == (piece.nut.x, piece.nut.y) and not piece.nut.status else self.symbols['SQUIRREL_WITH_NUT']

    def _render_flower(self, board_repr, piece):
        for (x, y) in piece.positions:
            board_repr[x][y] = self.symbols['FLOWER']

    def _display_board(self, board_repr):
        print("Current Board State:")
        for row in board_repr:
            print(" | ".join(row))
            print("-" * (len(row) * 4 - 1))
        print()

    def play(self):
        while True:
            # Render the board before each move
            self.render_board()

            print(Fore.CYAN + " Available pieces:")
            for idx, piece in enumerate(self.board.pieces):
                if isinstance(piece, Squirrel):
                    print(Fore.YELLOW + f"{idx}: {type(piece).__name__} at {piece.positions} with nut at {piece.nut} 🐿️")

            # Get user input for the piece index and direction
            piece_idx = int(input(Fore.GREEN + "🕹️ Choose the piece index to move (or -1 to quit): "))
            if piece_idx == -1:
                print(Fore.RED + "Game exited. 🛑")
                break

            piece = self.board.pieces[piece_idx]

            direction = input(Fore.GREEN + "➡️ Enter direction (UP, DOWN, LEFT, RIGHT): ").upper()
            if direction not in ["UP", "DOWN", "LEFT", "RIGHT"]:
                print(Fore.RED + "❌ Invalid direction! Please choose again.")
                continue

            # Check if the move is valid and execute it
            if self.board.can_move(piece, direction):
                self.board.move_piece(piece, direction)
                print(Fore.GREEN + "✅ Move successful.")
            else:
                print(Fore.RED + "❌ Move blocked! Try a different piece or direction.")

            # Check if the game has ended
            if self.board.is_game_end():
                self.render_board()
                print(Fore.MAGENTA + "🎉 Congratulations! All nuts are in holes. 🏆")
                break
