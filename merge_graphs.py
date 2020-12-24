import networkx as nx

def merge_graphs(graph1, graph2):
    edges1 = graph1.edges
    edges2 = graph2.edges 
    diff1 = edges1 - edges2
    if diff1==edges1:
        return nx.compose(graph1,graph2)
    else:
        common_edges = list(edges1 - diff1)
        for edges in common_edges:
            graph1[edges[0]][edges[1]]['weight'] += graph2[edges[0]][edges[1]]['weight']
        return nx.compose(graph2, graph1)

if __name__ == '__main__':
    G = nx.Graph()
    F = nx.Graph()
    E = nx.Graph()
    ed1 = [(1,2,1),(1,3,2),(2,3,1)]
    ed2 = [(1,3,1),(3,4,2),(2,4,1)]
    ed3 = [(4,5,1),(5,6,2),(4,6,1)]
    F.add_weighted_edges_from(ed2)
    E.add_weighted_edges_from(ed3)
    G2 = G
    print(merge_graphs(G,E).edges)
    print(merge_graphs(G2,F)[1][3])
    print(len(G2.nodes))