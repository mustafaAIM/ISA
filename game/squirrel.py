class Squirrel:
    def __init__(self, positions, nut): 
        self.positions = positions
        self.nut = nut

    def move(self, direction): 
        self.positions = [self._move_position(pos, direction) for pos in self.positions]
        self.nut.x ,self.nut.y = self._move_position((self.nut.x , self.nut.y), direction)

    def _move_position(self, position, direction): 
        x, y = position
        if direction == "UP":
            return x - 1, y
        elif direction == "DOWN":
            return x + 1, y
        elif direction == "LEFT":
            return x, y - 1
        elif direction == "RIGHT":
            return x, y + 1
    
    def __eq__(self, value):
        if not isinstance(value, Squirrel):
          return False
        return (self.positions == value.positions and self.nut == value.nut)
