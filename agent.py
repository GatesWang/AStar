import heapq
import math
from state import State

class Agent:
    def __init__(self, row, col, target_row, target_col):
        self.row = row
        self.col = col
        self.target_row = target_row
        self.target_col = target_col
        
        self.open_list = []
        self.closed_list = []
        self.start_state = None
        self.goal_state = None
        
    def get_location(self):
        return (self.row, self.col)
        
    def a_star_search(self, env):
        counter = 0
        self.start_state = State(self.row, self.col)
        self.goal_state = State(self.target_row, self.target_col)

        while self.start_state != self.goal_state:
            counter +=1
            self.start_state.set_g(0)
            self.start_state.set_search(counter)
            self.goal_state.set_g(math.inf)
            self.goal_state.set_search(counter)
            
            self.open_list = []
            self.closed_list = []
            
            self.start_state.set_f(self.start_state.g,  env.manhattan_distance(self.row,
                                                                               self.col,
                                                                               self.target_row,
                                                                               self.target_col))
            heapq.heappush(self.open_list, self.start_state)
            self.compute_path(env)
            if len(open_list)==0:
                print("no path")
                return;
            else:
                #follow tree pointers
                print(closed_list)
                #set start_state to current state of agent
                #update increased action costs
                pass
        return
        
    def compute_path(self, env):
        s = heapq.heappop(self.open_list)
        
        while self.goal_state.get_g() > s.get_g():
            print(len(self.open_list))
            if s not in self.closed_list:
                self.closed_list.append(s)          
            neighbors = env.get_neighbors(s.get_location())

            for neighbor in neighbors:
                neighbor_state = State(neighbor[0],neighbor[1])
                for state in self.open_list:
                    if state.get_location() == neighbor:
                        neighbor_state = state
                        break;
                
                if  neighbor_state.get_search() < self.goal_state.get_search():
                    neighbor_state.set_g(math.inf)
                    neighbor_state.set_search(self.goal_state.get_search())
                if neighbor_state.get_g() > s.get_g() + 1:
                    neighbor_state.set_g(s.get_g() + 1)
                    neighbor_state.set_tree(s)
                    if neighbor_state not in self.open_list:
                        heapq.heappush(self.open_list, neighbor_state)
                        
            s = heapq.heappop(self.open_list)


                    
                              

            

        

