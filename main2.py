from collections import deque
import networkx as nx


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()

    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

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

print("BFS: ")
bfs_recursive(G, deque(["Сільпо"]))
print("\n")
print("DFS: ")
dfs_recursive(G, 'Сільпо')
