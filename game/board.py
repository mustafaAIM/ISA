from squirrelL import SquirrelL
from squirrel import Squirrel
from flower import Flower
from hole import Hole
from colorama import *
import copy
from render import BoardRenderer

class Board:
    def __init__(self, size=(4, 4),renderer = None):
        self.size = size
        self.pieces = []  
        self.states = []  
        self.holes = [Hole(1,0,False),Hole(0,2,False),Hole(2,1,False),Hole(3,3,False)]
        self.renderer =  renderer or BoardRenderer()

    def __eq__(self,value):
        if not isinstance(value, Board):
            return False
        return (self.pieces == value.pieces and self.holes == value.holes)

    def add_piece(self, piece): 
        self.pieces.append(piece)

    def can_move(self, piece, direction):  
        for position in piece.positions:
            new_position = self._get_new_position(position, direction) 
            if not self._is_within_bounds(new_position) or self._is_occupied(new_position,piece):
                return False
        return True

    def _get_new_position(self, position, direction): 
        x, y = position
        if direction == "UP":
            return x - 1, y
        elif direction == "DOWN":
            return x + 1, y
        elif direction == "LEFT":
            return x, y - 1
        elif direction == "RIGHT":
            return x, y + 1

    def _is_within_bounds(self, position): 
        x, y = position
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def _is_occupied(self, position , checked_piece): 
        for piece in self.pieces:
            if position in piece.positions and not position in checked_piece.positions:
                return True
        return False

    def move_piece(self, piece, direction): 
        if self.can_move(piece, direction):
            piece.move(direction)
            for hole in self.holes:
                if (piece.nut.x , piece.nut.y) == (hole.x,hole.y) and (not hole.status) and (not piece.nut.status):
                    piece.nut.status = True
                    hole.status = True 
            # self.states.append(copy.deepcopy(self)) 
            # print(len(self.states))
        

    def get_state(self): 
        return [(piece.positions, piece.nut, type(piece).__name__) for piece in self.pieces]

    def is_game_end(self): 
        for piece in self.pieces: 
            if isinstance(piece, Squirrel) and not piece.nut.status:
                return False 
            
        with open("States.txt", 'a', encoding='utf-8') as file:
            for state in self.states:  
                  file.write(str([p for p in state.pieces]))
        return True

    def print_board(self): 
        self.renderer.render_board(self.size, self.pieces, self.holes)