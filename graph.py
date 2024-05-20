# Graph implemented via adjacency matrix
class Graph:

    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.matrix = [[0 for x in range(vertices)] for y in range(vertices)]

    def connected(self) -> bool:
        pass

    def regular(self) -> bool:
        pass

    def complete(self) -> bool:
        pass

    def bipartite(self) -> bool:
        pass


    def isCycle(self) -> bool:

        #TODO
        pass

    # Adds unweighted edge in undirected graph
    # Runs in O(1)
    def addEdge(self, x, y) -> None:

        # Verify vertices exist
        if x >= self.vertices or y >= self.vertices:
            print("ERROR: Vertex does not exist")
            return
        
        self.matrix[y][x] = 1
        self.matrix[x][y] = 1

    # Removes edge in undirected graph
    # Runs in O(1)
    def removeEdge(self, x, y) -> None:
        # Verify vertices exist
        if x >= self.vertices or y >= self.vertices:
            print("ERROR: Vertex does not exist")
            return
        
        self.matrix[y][x] = 0
        self.matrix[x][y] = 0

    def addVertex(self) -> None:
        self.vertices += 1

        # Initialize new edges to 0
        self.matrix.append([0] * self.vertices)
        for i in range(self.vertices - 1):
            self.matrix[i].append(0)
        

    # The most costly operation in matrix implementation and runs in O(n) where n is num elements
    # If frequent removes, linked list is better data structure
    def removeVertex(self, vertex: int) -> None:

        # Verify vertex exists
        if vertex >= self.vertices:
            print("ERROR: Vertex does not exist")
            return
        
        # Initialize new array
        array = [[0 for x in range(self.vertices - 1)] for y in range(self.vertices - 1)]
        self.vertices -= 1

        # Copy values into new array while deleting necessary rows
        # For undirected graphs, could cut compute time by only going over top half of matrix since they're identical across (0,0) (1,1) etc axis
        for i in range(0, self.vertices):
            for j in range(0, self.vertices):
                if i < vertex:
                    if j < vertex:
                        array[i][j] = self.matrix[i][j]
                    else:
                        array[i][j] = self.matrix[i][j + 1]
                elif j < vertex:
                    array[i][j] = self.matrix[i + 1][j]
                else:
                    array[i][j] = self.matrix[i + 1][j + 1]
        
        self.matrix = array

    def dfs_recursive(self, v: int, visited: list) -> None:
        visited[v] = True
        print(v, end=' ')

        for i in range(self.vertices):
            if self.matrix[v][i] == 1 and not visited[i]:
                self.dfs_recursive(i, visited)

    # Because implemented as adjacency matrix, bfs is O(V^2)
    def dfs(self, start_vertex: int = 0) -> None:

        visited = [False] * self.vertices
        self.dfs_recursive(start_vertex, visited)
        

    # Because implemented as adjacency matrix, bfs is O(V^2)
    def bfs(self, start_vertex: int = 0) -> None:
        
        visited = [False] * self.vertices

        queue = []
        queue.append(start_vertex)
        visited[start_vertex] = True

        while queue:

            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in range(self.vertices):
                if self.matrix[vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
            

    def printMatrix(self) -> None:
        print("\n\n Matrix:", end = "")
        for i in range(0, self.vertices):
            print()
            for j in range(0, self.vertices):
                print("", self.matrix[i][j], end = "")