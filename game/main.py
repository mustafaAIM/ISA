from board import Board
from flower import Flower
from squirrel import Squirrel
from squirrelL import SquirrelL
from nut import Nut
from render import BoardRenderer
import copy

renderer = BoardRenderer()
board = Board(size=(4, 4),renderer = renderer)


flower1 = Flower((3,3 )) 
board.add_piece(flower1) 

squirrel_L = SquirrelL(positions=[(0, 0), (1, 0), (0, 1)], nut=Nut(0,0,False))
squirrel_L_2 = SquirrelL(positions=[(3, 1), (3, 2), (2, 2)], nut=Nut(3,1,False))
squirrel_1x2 = Squirrel(positions=[(2, 0), (2, 1)], nut=Nut(2,0,False))
board.add_piece(squirrel_L)
board.add_piece(squirrel_1x2) 
board.add_piece(squirrel_L_2) 
renderer.play(board=board)


# board2 = copy.deepcopy(board)
# print(board == board2)