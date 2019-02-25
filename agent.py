import heapq
import math
from state import State

class Agent:
    def __init__(self, start_row, start_col, target_row, target_col, env):
        self.start_row = start_row
        self.start_col = start_col
        self.target_row = target_row
        self.target_col = target_col
        self.env = env
        
        self.open_list = []
        self.closed_list = []
        self.iterations = 0
        #print(self.start_row,self.start_col)
        
    def a_star_search(self):
        
        self.current_state = State(self.start_row, self.start_col)
        self.goal_state = State(self.target_row, self.target_col)


        self.current_state.set_g(0)
        self.current_state.set_f(self.current_state.g,  self.env.manhattan_distance(self.start_row,
                                                                                    self.start_col,
                                                                                    self.target_row,
                                                                                    self.target_col))
        heapq.heappush(self.open_list, self.current_state)
        while True:
            self.iterations+=1
            self.expand_lowest()
            if self.current_state.get_location() == self.goal_state.get_location():
                print("found path, # iterations: " + str(self.iterations))
                return
            if len(self.open_list)==0:
                print("no path # iterations: " + str(self.iterations))
                return
        
    def expand_lowest(self):
        s = heapq.heappop(self.open_list)
        #print(s)
        self.current_state = s
        if s.get_location() == (self.target_row,self.target_col):
            return
        
        if s not in self.closed_list:
            self.closed_list.append(s.get_location())          
            neighbors = self.env.get_neighbors(s.get_location())

            #print(neighbors)
            for neighbor in neighbors:
                
                if neighbor not in self.closed_list:
                    if neighbors[neighbor] == 0 or neighbors[neighbor] == 10:
                        #either get reference to neighbor_state in open list or create new 
                        neighbor_state = State(neighbor[0],neighbor[1])
                        for state in self.open_list:
                            if state.get_location() == neighbor:
                                neighbor_state = state
                                break;
                            
                        neighbor_state.set_parent(s)
                        if neighbor_state.get_g() > s.get_g() + 1:
                            neighbor_state.set_parent(s)
                            neighbor_state.set_f(s.get_g() + 1,  self.env.manhattan_distance(neighbor[0],
                                                                                             neighbor[1],
                                                                                             self.target_row,
                                                                                             self.target_col))
                            if neighbor_state not in self.open_list:
                                heapq.heappush(self.open_list, neighbor_state)
            #print(self.open_list)
            #print("-----------------------")

    def color_grid(self):
        state = self.current_state
        while state.get_parent() != None:
            #print(state.get_parent().get_location())
            row, col = state.get_location()
            self.env.change_block(row,col)
            state = state.get_parent()

        


                    
                              

            

        

