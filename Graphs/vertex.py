class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def __repr__(self) -> str:
        return self.value

    def add_edge(self, vertex, weight = 0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())