import pandas as pd
import numpy as np
import math
import sys
from operator import itemgetter
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self,vertexNum,edges,nodes):
        self.edges=edges
        self.nodes=nodes
        self.vertexNum=vertexNum
        self.MST=[]

    def printSolution(self):
        print("Edge: Weight")
        for s,d,w in self.MST:
            print(s,"    ",d,"     ",w)
    
    def Cluster(self, n):
        distlst = []
        for s, w, d in self.MST:
            distlst.append([s, w, d])
        sortlist = sorted(distlst, key=itemgetter(2))
        newMst = sortlist[n:]  # Select the first 'n' elements from the sorted list
        return newMst
    
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

def Euclidean(x,y,z,w):
    return math.sqrt(math.pow(x-z,2)+math.pow(y-w,2))

    
data=pd.read_csv('D:\coding\PRML\lab4\iris.csv')

test=data[["SepalLengthCm","SepalWidthCm"]]

edges=[]
for index1,row1 in test.iterrows():
    lst=[]
    for index2, row2 in test.iterrows():
        lst.append(Euclidean(row1["SepalLengthCm"],row1["SepalWidthCm"],row2["SepalLengthCm"],row2["SepalWidthCm"]))
    edges.append(lst)

cnt=test["SepalLengthCm"].count()
nodes=[]
for x in range(cnt):
    nodes.append(x)
    x+=1
    
g1=Graph(cnt,edges,nodes)
g1.Prims()

cluster_parameter = int(input("Enter the number of clusters you need: "))  # Assuming the user enters 3
finalMst = g1.Cluster(cluster_parameter)  # Clustering into 3 groups

G_mst = nx.Graph()

for s, d, w in finalMst:
    G_mst.add_node(s)
    G_mst.add_node(d)
    G_mst.add_edge(s, d, weight=w)

layout = nx.spring_layout(G_mst)    

# Create a dictionary to map nodes to their cluster index
cluster_map = {}
cluster_index = 0

for s, d, _ in finalMst:
    if s not in cluster_map:
        cluster_map[s] = cluster_index
        cluster_index += 1
    if d not in cluster_map:
        cluster_map[d] = cluster_index
        cluster_index += 1

# Create a list of colors for nodes based on their cluster index
cluster_colors = ['red', 'blue', 'green']  # Add more colors if needed
node_colors = [cluster_colors[cluster_map[node]] for node in list(G_mst.nodes())]

nx.draw(G_mst, pos=layout, with_labels=False, font_weight='normal', node_size=100, node_color=node_colors)

nx.draw_networkx_edges(G_mst, pos=layout, width=2, edge_color='green')

edge_labels = {(s, d): f'{w:.2f}' for s, d, w in finalMst}
nx.draw_networkx_edge_labels(G_mst, pos=layout, edge_labels=edge_labels)

plt.show()