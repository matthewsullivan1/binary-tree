class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        """Add an edge between vertices u and v."""
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
    
    def getAdj(self, v):
        return self.adjacency_list[v]

    def dfs(self, source):
        marked = [False for _ in range(self.vertices)]
        search_result = []
        self._dfs(source, marked, search_result)
        return search_result

    def _dfs(self, v, marked, search_result):
        marked[v] = True
        search_result.append(v)
        #print(v)

        for vertice in self.adjacency_list[v]:
            if not marked[vertice]:
                self._dfs(vertice, marked, search_result)
                #print(vertice)

    def bfs(self, source):
        marked = [False for _ in range(self.vertices)]
        search_result = []
        queue = []

        marked[source] = True
        queue.append(source)

        while len(queue) != 0:
            curr = queue.pop()
            #print(curr)
            search_result.append(curr)

            for vertice in self.adjacency_list[curr]:
                if not marked[vertice]:
                    marked[vertice] = True
                    queue.append(vertice)
        return search_result
    
if __name__ == '__main__':
# Create a graph with 20 vertices
    graph = Graph(20)

    # Add edges (change as needed)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(3, 7) 
    graph.add_edge(3, 8)
    graph.add_edge(4, 9)
    graph.add_edge(4, 10)
    graph.add_edge(5, 11)
    graph.add_edge(5, 12)
    graph.add_edge(6, 13)
    graph.add_edge(6, 14)
    graph.add_edge(7, 15)
    graph.add_edge(7, 16)
    graph.add_edge(8, 17)
    graph.add_edge(8, 18)
    graph.add_edge(9, 19)

    # Test DFS and BFS from a source vertex
    print("DFS from vertex 0:", graph.dfs(2)) 
    print("BFS from vertex 2:", graph.bfs(2))
