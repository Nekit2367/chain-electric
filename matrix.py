class Vertex():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y

    def Print(self):
        print(f"({int(self.x):3}, {int(self.y):3})".ljust(10))

class Matrix():
    def __init__(self, n, m):
        self.n = int(n)
        self.m = int(m)
        self.vertexes = [[0 for j in range(self.m)] for i in range(self.n)]

    def SetVertex(self, vertex, i, j):
        self.vertexes[i][j] = vertex

    def GetVertexes(self):
        return self.vertexes
    
    def Print(self):
        for i in range(self.n):
            for j in range(self.m):
                x = int(self.GetVertexes()[i][j].GetX())
                y = int(self.GetVertexes()[i][j].GetY())

                print(f"({x:3}, {y:3})".ljust(10), end='    ')

            print()