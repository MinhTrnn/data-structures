from collections import defaultdict

class AdjList:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def display(self):
        for key, values in self.adj_list.items():
            print(f'{key}: {values}')

    def add_edge(self, start, end):
        self.adj_list[start].append(end)
        self.adj_list[end].append(start)

    def remove_edge(self, start, end):
        if end in self.adj_list[start] and start in self.adj_list[end]:
            self.adj_list[start].remove(end)
            self.adj_list[end].remover(start)

if __name__=="__main__":
    graph = AdjList(5)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.display()