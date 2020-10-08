import heapq
import math
from state import State
from map import Map

class Agent:
    def __init__(self, start, target, map, weight):
        self.map = map
        self.open_list = []
        self.closed_list = {}
        self.iterations = 0
        self.weight = weight
        print("using weight: " + str(self.weight))

        self.current_state = State(start)
        self.goal_state = State(target)
        self.current_state.set_f(0, self.calculate_h(self.current_state))

        heapq.heappush(self.open_list, self.current_state)

    def search(self):
        while True:
            self.iterations+=1
            self.compute_path()
            if self.current_state.get_location() == self.goal_state.get_location():
                print("found path, # iterations: " + str(self.iterations))
                print(self.current_state.g)
                return
            if len(self.open_list)==0:
                print("no path # iterations: " + str(self.iterations))
                print(self.current_state.g)
                return

    def compute_path(self):
        state = heapq.heappop(self.open_list)
        self.current_state = state
        location = state.get_location()
        if location == self.goal_state.get_location() or state in self.closed_list:
            return

        self.closed_list[location] = state
        neighbors = self.map.get_neighbors(location)
        self.procces_neighbors(neighbors)

    def procces_neighbors(self, neighbors):
        for neighbor in neighbors:
            if neighbor in self.closed_list:
                continue

            if self.map.get_block(neighbor) > self.map.river:
                continue

            neighbor_state = self.get_from_open_list(neighbor)
            self.update_in_open_list(neighbor_state)

    def update_in_open_list(self, neighbor_state):
        parent = neighbor_state.get_parent()
        if parent == None:
            neighbor_state.set_parent(self.current_state)
            parent = self.current_state

        new_g = self.calculate_g(parent, neighbor_state);
        if neighbor_state.get_g() > new_g:
            neighbor_state.set_f(new_g,  self.calculate_h(neighbor_state))
            try:
                pass
            except:
                pass
            if neighbor_state not in self.open_list:
                heapq.heappush(self.open_list, neighbor_state)

    def calculate_h(self, state):
        location = state.get_location()
        location_target = self.goal_state.get_location()
        return self.weight * self.map.manhattan_distance(location, location_target)

    def calculate_g(self, parent, neighbor):
        p_location = parent.get_location()
        g = parent.get_g()
        n_location = neighbor.get_location()
        p_block = self.map.get_block(p_location)
        n_block = self.map.get_block(n_location)

        p_hard = p_block == self.map.hard
        n_hard = n_block == self.map.hard
        p_river = p_block == self.map.river
        n_river = n_block == self.map.river

        both_hard = p_hard and n_hard
        one_hard = p_hard ^ n_hard
        both_river = p_river and n_river

        diagonal = False
        if self.map.manhattan_distance(p_location, n_location) == 2:
            diagonal = True

        from math import sqrt
        if both_hard:
            if diagonal:
                g += sqrt(8)
            else:
                g += 2
        elif one_hard:
            if diagonal:
                g += .5 * (sqrt(2) + sqrt(8))
            else:
                g += 1.5
        else:
            if diagonal:
                g += sqrt(2)
            else:
                g += 1

        if both_river:
            g *= (.25)

        return g

    def get_from_open_list(self, neighbor):
        for state in self.open_list:
            if state.get_location() == neighbor:
                return state

        return State(neighbor)

    def color_map(self):
        state = self.current_state
        while state.get_parent() != None:
            #print(state.get_parent().get_location())
            self.map.set_block(state.get_location(), self.map.traversed)
            state = state.get_parent()
