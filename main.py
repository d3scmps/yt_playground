import casanova
import os 
import networkx as nx
import time
from matrice_adj import mat_adj_vid 
from merge_graphs import merge_graphs
from tqdm import tqdm
# get all csv files
#os commands

# handle 3 videos  per 3 videos : 1 graph per 3 videos and then merge the graphs. 
d = time.time() + 100
os.chdir('csv')
fichiers = os.popen('ls').read().split('\n')
### 
list_ids = []
###propre au fichier 
for fichier in fichiers:
    if not(fichier):
        continue
    new_id = set()
    with open(fichier) as f:
        reader = casanova.reader(f)
        for idd in reader.cells('author_channel_id'): #check order 
            new_id.add(idd)#str cost more than int, but id is 
    list_ids.append(new_id)

liste_graphes = []
A = ''
s = 0
for ids in tqdm(list_ids):
    s += len(ids)
    if type(A)==str:
        A = mat_adj_vid(A,ids)
    if A.size > 1500:
        #create G from A
        G = nx.Graph()
        G.add_nodes_from(A.columns)
        col = A.columns
        for c in col:
            z = A[c]
            for i in     z.index:
                G.add_edge(c,i,weight=z[i])
        liste_graphes.append(G)
        del G
        A = mat_adj_vid('', ids)
    else:
        A = mat_adj_vid(A,ids)

G = nx.Graph()
G.add_nodes_from(A.columns)
col = A.columns
for c in col:
    z = A[c]
    for i in z.index:
        G.add_edge(c,i,weight=z[i])
liste_graphes.append(G)
    
del G
del A 
del list_ids
print(len(liste_graphes))

FinalGraph = nx.Graph()
while len(liste_graphes)!=0:
    FinalGraph  = merge_graphs(FinalGraph,liste_graphes.pop())

print(s)
print(len(FinalGraph.nodes))

# merge graph ? 
#liste de matrices, vérifier la taille. 

"""
while len(list_ids)!=0:
    if time.time() > d:
        break
    print('ok')
    list_ids.pop(len(list_ids)-1)
    #
"""
"""
for x in tqdm(list_ids):
    time.sleep(0.01)
    A = mat_adj_vid(A,x)
print(s)
print(len(A.index))
"""
### networkx 

""" 
-- add edges with weight (node1,node2, weight)
G.add_weighted_edges_from([(1,2,1),(1,4,1),(3,4,1),(4,2,1)])
--- weight : poids de l'arc
G.add_edge(1, 2, weight=4.7 )
--- permet d'ajouter des noeuds avec des attributs ! 
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])"""
