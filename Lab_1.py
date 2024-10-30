def orientation(p, q, r):
    """Вычисление ориентации для трёх точек.
    0 -> коллинеарные
    1 -> по часовой стрелке
    2 -> против часовой стрелки
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex_hull(points):
    """Поиск выпуклой оболочки методом Джарвиса"""
    n = len(points)
    if n < 3:
        return points  # Выпуклая оболочка невозможна

    hull = []

    # Находим самую левую точку
    leftmost = 0
    for i in range(1, n):
        if points[i][0] < points[leftmost][0]:
            leftmost = i

    p = leftmost
    while True:
        hull.append(points[p])

        # Ищем точку q такую, что все точки находятся справа от вектора p->q
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q  # Переходим к следующей вершине

        if p == leftmost:  # Замкнули оболочку
            break

    return hull

# Пример использования
points = [(0, 3), (2, 3), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
hull = convex_hull(points)
print("Точки выпуклой оболочки:", hull)
