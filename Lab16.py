# ДИСКРЕТНАЯ ЗАДАЧА ОБ УКЛАДКЕ РЮКЗАКА
def knapsack(weights, values, capacity):
    n = len(weights)
    #создаем таблицу для хранения максимальных ценностей
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    #заполняем таблицу dp
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # выбираем максимальное значение, взять или нет
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                #если не можем взять предмет
                dp[i][w] = dp[i - 1][w]
# максимальная ценность в правом нижнем углу таблицы
    return dp[n][capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity)) 
