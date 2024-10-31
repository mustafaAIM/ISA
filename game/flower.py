class Flower:
    def __init__(self, position):
        self.positions = [position]  
    def __eq__(self, other):
       if not isinstance(other, Flower): 
          return False 
       return self.positions == other.positions
