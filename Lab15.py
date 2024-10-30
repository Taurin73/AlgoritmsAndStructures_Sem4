def greedy_coloring(graph):
    # Количество вершин в графе
    num_vertices = len(graph)    
    # Массив для хранения цвета каждой вершины
    result = [-1] * num_vertices    
    # Первый цвет назначаем первой вершине
    result[0] = 0    
    # Список доступных цветов
    available_colors = [True] * num_vertices    
    # Раскраска остальных вершин
    for u in range(1, num_vertices):
        # Отмечаем цвета соседей как недоступные
        for neighbor in graph[u]:
            if result[neighbor] != -1:
                available_colors[result[neighbor]] = False        
        # Находим первый доступный цвет
        for color in range(num_vertices):
            if available_colors[color]:
                result[u] = color
                break        
        # Сбрасываем доступные цвета для следующей вершины
        available_colors = [True] * num_vertices
    
    return result

# Пример графа в виде списка смежности
graph = [
    [1, 2],      # Вершина 0 соединена с 1 и 2
    [0, 2, 3],   # Вершина 1 соединена с 0, 2 и 3
    [0, 1],      # Вершина 2 соединена с 0 и 1
    [1, 4],      # Вершина 3 соединена с 1 и 4
    [3]          # Вершина 4 соединена с 3
]

# Получаем раскраску графа
colors = greedy_coloring(graph)

# Вывод результата
for vertex, color in enumerate(colors):
    print(f"Вершина {vertex} имеет цвет {color}")
