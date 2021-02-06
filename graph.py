class Graph(): 

    def __init__(self):
        self.num_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.num_of_nodes += 1


    def add_edge(self, node1, node2):  # Undirected graph
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connection(self):
        for x in self.adjacent_list:
            print(x, end = ' --> ')
            for i in self.adjacent_list[x]:
                print(i, end = ' ') 
            print()


# Testing
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_edge(3, 1)
g.add_edge(3, 4)
g.add_edge(4, 2) 
g.add_edge(4, 5) 
g.add_edge(1, 2) 
g.add_edge(1, 0) 
g.add_edge(0, 2) 
g.add_edge(6, 5)
g.show_connection()