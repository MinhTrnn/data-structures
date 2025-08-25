class AdjMatrixGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = []

        for i in range(vertices):
            row = []
            for j in range(vertices):
                row.append(0)
            self.adj_matrix.append(row)

    def display(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.adj_matrix[i][j], end = ' ')
            print()

    def add_edge(self,u ,v):
        self.adj_matrix[u][v] += 1
        self.adj_matrix[v][u] += 1   #undirected graph

    def remove_edge(self,u ,v):
        self.adj_matrix[u][v] -= 0
        self.adj_matrix[v][u] -= 0   #undirected graph

if __name__=="__main__":
    graph = AdjMatrixGraph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,1)
    graph.display()