#ford fulkerson
import networkx as nx
def minFlow(G,path):
  min_flow=100
  for i in range(0,len(path)-1):
    temp=G[path[i]][path[i+1]]['weight']
    if min_flow>temp:
      min_flow=temp
  return min_flow
G=nx.DiGraph()
G.add_weighted_edges_from([('S', 'A', 4), ('A', 'B', 4), ('B', 'T', 2), ('S', 'C', 3), ('C', 'D', 6), ('D', 'T', 6), ('B', 'C', 3)])
paths=nx.all_simple_paths(G,'S','T')
max_flow=0
for path in paths:
  temp=minFlow(G,path)
  print("For path ", path, " having min flow ", temp)
  for i in range(0,len(path)-1):
    G[path[i]][path[i+1]]['weight']-=temp
  max_flow+=temp
print('Max Flow-',max_flow)