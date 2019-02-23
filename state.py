import math

class State:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g = math.inf
        self.f = 0
        self.h = 0
        self.h_new = 0 
        self.parent = None

    #setters 
    def set_g(self, g):
        self.g = g
        self.f = self.g+self.h
    
    def set_h(self, h):
        self.h = h
        self.f = self.g+self.h
        
    def set_f(self, g, h):
        self.g = g
        self.h = h
        self.f = g + h
        
    def set_parent(self, parent):
        self.parent = parent
    
    #getters
    def get_location(self):
        return (self.row, self.col)
    
    def get_g(self):
        return self.g
    
    def get_h(self):
        return self.h
    
    def get_f(self):
        return self.f

    def get_parent(self):
        return self.parent

    #override some methods
    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
        rep = "(" + str(self.row) + "," + str(self.col) + ") " + str(self.f)
        return rep

    def __repr__(self):
        rep = "(" + str(self.row) + "," + str(self.col) + ") " + str(self.f)
        return rep
