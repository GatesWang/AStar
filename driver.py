from environment import Environment
from agent import Agent
import pickle
import os.path


class Driver:
    #loads the mazes
    def __init__(self, size, name):
        self.start = (0,0)
        self.target = (size-1,size-1)
        self.size = size
        self.name = name
        self.env_list = []
        
        if os.path.isfile(self.name + '.pkl'):
            with open(self.name + '.pkl', 'rb') as f:
                self.env_list = pickle.load(f)  
        else:
            self.generate_mazes()


    def generate_mazes(self):
        for i in range(0,50):
            env = Environment(self.start[0],
                              self.start[1],
                              self.target[0],
                              self.target[1],
                              self.size)
            env_list.append(env)
            
        with open(self.name + '.pkl', 'wb') as f:
            pickle.dump(env_list, f)
        with open(self.name + '.pkl', 'rb') as f:
            self.env_list = pickle.load(f) 

    #shows the mazes, should not need to run
    def show_mazes(self):
        with open(self.name + '.pkl', 'rb') as f:
            self.env_list = pickle.load(f)
            for env in self.env_list:
                env.show_grid()
            
    #creates a new agent and runs it on env_list[i]
    def run_agent(self, i):
        start = self.start
        target = self.target
        env = self.env_list[i]
        #env.show_grid()
        print("forward")
        #foward
        agent = Agent(start[0],
                      start[1],
                      target[0],
                      target[1],
                      env)
        
        agent.forward_a_star_search()
        agent.color_grid()
        env.show_grid()
        env.reset_grid()

        print("backward")
        #backward
        agent = Agent(target[0],
                      target[1],
                      start[0],
                      start[1],
                      env)
        
        #env.show_grid()
        agent.forward_a_star_search()
        agent.color_grid()
        env.show_grid()
        env.reset_grid()
        
driver = Driver(100, "100x100")
for i in range(0,50):
    driver.run_agent(i)


    
    
