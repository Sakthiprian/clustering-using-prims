import sys

class Graph:
    def __init__(self,vertexNum,edges,nodes):
        self.edges=edges
        self.nodes=nodes
        self.vertexNum=vertexNum
        self.MST=[]

    def printSolution(self):
        print("Edge: Weight")
        for s,d,w in self.MST:
            print(s," ",d," ",w)
    
    def Prims(self):
        visited=[0]*self.vertexNum
        edgeNum=0
        visited[0]=True
        while edgeNum< self.vertexNum-1:
            min=sys.maxsize
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if (not(visited[j]) and self.edges[i][j]):
                            if min>self.edges[i][j]:
                                min=self.edges[i][j]
                                s=i
                                d=j
            self.MST.append([self.nodes[s],self.nodes[d],self.edges[s][d]])
            visited[d]=True
            edgeNum+=1
        self.printSolution()

edges=[[0,9,2,0,0,0,0,0],[9,0,4,0,2,0,0,0],[2,4,0,2,3,0,0,0],[0,0,2,0,3,11,0,0],[0,2,3,3,0,0,9,0],[0,0,0,11,0,0,5,0],[0,0,0,0,9,5,0,7],[0,0,0,0,11,0,7,0]]
nodes=["1","2","3","4","5","6","7","8"]
g=Graph(8,edges,nodes)
g.Prims()