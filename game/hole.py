class Hole:
    def __init__(self, x,y,status):
        self.x = x
        self.y = y
        self.status = status 

    def __eq__(self, value):
        return (self.x == value.x and self.y == value.y and self.status == value.status) 