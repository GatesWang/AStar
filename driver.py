from map import Map
from agent import Agent

class Driver:
    def __init__(self, num_maps, num_start_goal):
        self.num_maps = num_maps
        self.num_start_goal = num_start_goal

    def generate_maps(self):
        self.maps = []
        size = (120, 160)
        for i in range(self.num_maps):
            self.maps.append(Map(size))

    def map_to_text_file(self):
        for i in range(self.num_maps):
            self.print_map(i)
            self.print_map_versions(i)

    def print_map(self, i):
        name = "map" + str(i)
        f = open(name, 'w')
        map = self.maps[i]

        for center in map.hard_centers:
            f.write(str(center) + "\n")

        for i in range(map.max_row+1):
            for j in range(map.max_col+1):
                value = map.get_block()
                default = '1'
                out = map.get(value, default) + ' '
                f.write(out)
            f.write("\n")

    def print_map_versions(self, i):
        map = self.maps[i]

        for j in range(self.num_start_goal):
            map.generate_start_and_end()
            start, target = map.start, map.target
            name = "map" + str(i) + "_version_" + str(j)

            f = open(name, 'w')
            f.write(str(start) + "\n")
            f.write(str(target) + "\n")

    def text_files_to_map(self):
        for i in range(self.num_maps):
            name = "map" + str(i)
            self.read_map(name)

            for j in range(self.num_start_goal):
                name = "map" + str(i) + "_version_" + str(j)

    def run_agents(self):
        for map in self.maps:
            for j in range(self.num_start_goal):
                map.generate_start_and_end()
                start, target = map.start, map.target
                weights = [0, 1, 1.2, 2] #0 corresponds to uniform, 1 corresponds to a_star
                for weight in weights:
                    agent = Agent(start, target, map, weight)
                    agent.search()
                    agent.color_grid()

                    map.show_grid()
                    map.reset_grid()

driver = Driver(1,2)
driver.generate_maps()
driver.map_to_text_file()
driver.text_files_to_map()

#driver.run_agents()
