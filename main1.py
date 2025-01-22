import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ["Сільпо", "АТБ", "Фора", "Аврора", "НП", "Розетка", "Зал", "Метро"]
G.add_nodes_from(nodes)

edges = [
    ("Сільпо", "АТБ", 5),
    ("Сільпо", "Фора", 10),
    ("Сільпо", "НП", 7),
    ("АТБ", "Фора", 3),
    ("АТБ", "Аврора", 8),
    ("АТБ", "Розетка", 6),
    ("Фора", "Аврора", 2),
    ("Фора", "Зал", 4),
    ("Аврора", "Метро", 5),
    ("НП", "Розетка", 2),
    ("НП", "Метро", 8),
    ("Розетка", "Зал", 3),
    ("Зал", "Метро", 1)
]
G.add_weighted_edges_from(edges)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="pink", node_size=2000, font_size=10, font_weight="bold", font_color="blue")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']} км" for u, v, d in G.edges(data=True)})
plt.title("Лісовий масив")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
average_degree = sum(degrees.values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"  {node}: {degree}")
print(f"Середній ступінь вершин: {average_degree:.2f}")
