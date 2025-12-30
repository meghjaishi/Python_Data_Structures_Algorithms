class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.print_graph()
    print(my_graph.add_vertex("A"))  # Trying to add duplicate vertex


    