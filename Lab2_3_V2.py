import json
from collections import deque

# Чтение матрицы смежности из файла
with open('adjacency_matrix[test1].json', 'r') as file:
    adjacency_matrix = json.load(file)

# Функция для поиска кратчайших путей от заданной вершины до всех остальных вершин с помощью BFS
def bfs_shortest_paths(matrix, start_vertex):
    n = len(matrix)
    distances = [-1] * n  # -1 будет означать, что вершина недостижима
    distances[start_vertex] = 0
    queue = deque([start_vertex])
    
    while queue:
        v = queue.popleft()
        for i, is_adjacent in enumerate(matrix[v]):
            if is_adjacent and distances[i] == -1:  # Если есть ребро и вершина не посещена
                distances[i] = distances[v] + 1
                queue.append(i)
    
    return distances

# Функция для поиска компонент связности с помощью BFS
def bfs_connected_components(matrix):
    n = len(matrix)
    visited = [False] * n
    components = []
    
    for start_vertex in range(n):
        if not visited[start_vertex]:
            component = []
            queue = deque([start_vertex])
            visited[start_vertex] = True
            
            while queue:
                v = queue.popleft()
                component.append(v)
                for i, is_adjacent in enumerate(matrix[v]):
                    if is_adjacent and not visited[i]:
                        visited[i] = True
                        queue.append(i)
            
            components.append(component)
    
    return components

# Ввод и вывод результатов
start_vertex = 0  # Заданная вершина для поиска кратчайших путей
shortest_paths = bfs_shortest_paths(adjacency_matrix, start_vertex)
print(f"Кратчайшие пути от вершины {start_vertex}: {shortest_paths}")

connected_components = bfs_connected_components(adjacency_matrix)
print(f"Количество компонент связности: {len(connected_components)}")
print(f"Состав компонент связности: {connected_components}")
