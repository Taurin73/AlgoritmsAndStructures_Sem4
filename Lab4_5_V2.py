import json

# Чтение матрицы смежности из файла
with open('adjacency_matrix[test1].json', 'r') as file:
    adjacency_matrix = json.load(file)

# Функция для поиска компонент связности с помощью DFS
def dfs_connected_components(matrix):
    n = len(matrix)
    visited = [False] * n
    components = []
    
    def dfs(v, component):
        visited[v] = True
        component.append(v)
        for i, is_adjacent in enumerate(matrix[v]):
            if is_adjacent and not visited[i]:
                dfs(i, component)
    
    for vertex in range(n):
        if not visited[vertex]:
            component = []
            dfs(vertex, component)
            components.append(component)
    
    return components

# Функция для поиска сильно связных компонент в орграфе с помощью алгоритма Косарайю
def kosaraju_strongly_connected_components(matrix):
    n = len(matrix)
    visited = [False] * n
    order = []
    
    # Шаг 1: Проход DFS и создание порядка завершения вершин
    def dfs1(v):
        visited[v] = True
        for i, is_adjacent in enumerate(matrix[v]):
            if is_adjacent and not visited[i]:
                dfs1(i)
        order.append(v)
    
    # Шаг 2: Построение транспонированного графа
    transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
    
    # Шаг 3: Поиск компонент в обратном порядке с использованием транспонированного графа
    def dfs2(v, component):
        visited[v] = True
        component.append(v)
        for i, is_adjacent in enumerate(transposed_matrix[v]):
            if is_adjacent and not visited[i]:
                dfs2(i, component)
    
    # Запускаем первый DFS для записи порядка завершения
    for vertex in range(n):
        if not visited[vertex]:
            dfs1(vertex)
    
    # Обнуляем массив посещений перед вторым DFS
    visited = [False] * n
    scc = []
    
    # Запуск второго DFS в порядке убывания завершения
    while order:
        v = order.pop()
        if not visited[v]:
            component = []
            dfs2(v, component)
            scc.append(component)
    
    return scc

# Вывод результатов
# Для задачи 4: Компоненты связности в неориентированном графе
connected_components = dfs_connected_components(adjacency_matrix)
print(f"Количество компонент связности: {len(connected_components)}")
print(f"Состав компонент связности: {connected_components}")

# Для задачи 5: Сильно связные компоненты в ориентированном графе
strongly_connected_components = kosaraju_strongly_connected_components(adjacency_matrix)
print(f"Количество сильно связных компонент: {len(strongly_connected_components)}")
print(f"Состав сильно связных компонент: {strongly_connected_components}")
