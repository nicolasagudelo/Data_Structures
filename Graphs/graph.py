from vertex import Vertex

class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        print(f'Adding {vertex} to the graph')
        self.graph_dict[vertex.value] = vertex
    
    def add_edge(self, from_vertex, to_vertex, weight = 0):
        pass

grand_central = Vertex("Grand Central Station")

railway = Graph()

print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)