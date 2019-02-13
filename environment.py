import numpy as np
import matplotlib as mpl
import random
from matplotlib import pyplot

class Environment:
    def __init__(self, start_row, start_col, target_row, target_col, size):
        np.set_printoptions(threshold=np.nan)
        
        self.start_row = start_row
        self.start_col = start_col
        self.target_row = target_row
        self.target_col = target_col
        self.size = size

        self.generate_grid()

    def generate_grid(self):
        stack = []
        self.grid = np.zeros((self.size,self.size))
        visited = np.zeros((self.size,self.size))
        visited_count = 1
        
        rand_row = random.randint(0, self.size-1)
        rand_col = random.randint(0, self.size-1)
        visited[rand_row, rand_col] = 1
        self.grid[rand_row, rand_col] = 0
        neighbors = self.get_neighbors((rand_row, rand_col))
        
        for neighbor in neighbors.keys():
            rand = random.randint(1, 10)
            if rand<=3:
                self.grid[neighbor] = 1
            else:
                stack.append(neighbor)
            visited[neighbor] = 1
            visited_count+=1

        while visited_count!=self.size**2:
            if len(stack)==0:
                for i in range(0,self.size):
                    for j in range(0,self.size):
                        if visited[(i,j)] == 0:
                            visited[(i,j)] = 1
                            visited_count+=1
                            stack.append((i,j))
                            break
            
            block = stack.pop(len(stack)-1)
            neighbors = self.get_neighbors(block)
            for neighbor in neighbors.keys():
                if visited[neighbor]==1:
                    continue
                else:
                    rand = random.randint(1, 10)
                    if rand<=3:
                        self.grid[neighbor] = 1
                    else:
                        stack.append(neighbor)
                    visited[neighbor] = 1
                    visited_count+=1

        self.grid[self.start_row][self.start_col] = -10
        self.grid[self.target_row][self.target_col] = 10
        
    def show_grid(self):
        cmap = mpl.colors.ListedColormap(['red','white','black','blue'])
        bounds=[-20, -1, .5, 1.5, 20]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        img = pyplot.imshow(self.grid,
                            interpolation='nearest',
                            cmap = cmap,
                            norm=norm)
        pyplot.show()
        
    def get_neighbors(self, block):
        row = block[0]
        col = block[1]
        neighbors = {}
        if row-1>0:
            neighbors[(row-1,col)] = self.grid[row-1][col]
        if row+1<self.size-1:
            neighbors[(row+1,col)] = self.grid[row+1][col]
        if col-1>0:
            neighbors[(row,col-1)] = self.grid[row][col-1]
        if col+1<self.size-1:
            neighbors[(row,col+1)] = self.grid[row][col+1]
        return neighbors
    
    def manhattan_distance(self, row1, col1, row2, col2):
        return abs(row1-row2) + abs(col1-col2)

    
