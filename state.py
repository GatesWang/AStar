class State:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.search = 0
        self.g = 0
        self.f = 0
        self.h = 0
        self.tree = None

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

    def set_search(self, search):
        self.search = search
        
    def set_tree(self, tree):
        self.tree = tree
    
    #getters
    def get_location(self):
        return (self.row, self.col)
    
    def get_g(self):
        return self.g
    
    def get_h(self):
        return self.h
    
    def get_f(self):
        return self.f
    
    def get_search(self):
        return self.search

    def get_tree(self):
        return self.tree

    #override some methods
    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.get_location() == other.get_location()

    def __str__(self):
        rep = "(" + str(self.row) + "," + str(self.col) + ") " + str(self.f)
        return rep
