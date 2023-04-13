import networkx as nx

# Crear el grafo
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2, weight=0.5)
G.add_edge(2, 3, weight=1.0)
G.add_edge(1, 3, weight=0.8)

# Implementar el algoritmo de Prim
T = nx.minimum_spanning_tree(G)

# Mostrar el árbol resultante
print(T.edges())