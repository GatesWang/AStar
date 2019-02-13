from environment import Environment
from agent import Agent
import pickle

class Driver:
    #loads the mazes
    def __init__(self, size):
        self.start = (0,0)
        self.size = 11
        self.target = (size-1,size-1)
        #with open('mazes.pkl', 'rb') as f:
        #    self.env_list = pickle.load(f)
            
    #generates the mazes, should not need to run
    def generate_mazes(self, name):
        env_list = []
        for i in range(0,50):
            env = Environment(self.start[0],
                              self.start[1],
                              self.target[0],
                              self.target[1],
                              self.size)
            env_list.append(env)
            
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(env_list, f)

    def show_mazes(self, name):
        with open(name + '.pkl', 'rb') as f:
            self.env_list = pickle.load(f)
            for env in self.env_list:
                env.show_grid()
            
    #creates a new agent and runs it on env_list[i]
    def run_agent(self, i):
        start = self.start
        target = self.target
        agent = Agent(start[0],
                      start[1],
                      target[0],
                      target[1])
        
        env = self.env_list[i]        
        agent.a_star_search(env)

driver = Driver(11)
driver.generate_mazes("test2")
driver.show_mazes("test2")
#driver.run_agent(0)

    
    
