def bin_packing(items, bin_capacity):
    # Сортируем предметы в порядке убывания
    items.sort(reverse=True)

    # Список для хранения оставшейся вместимости ящиков
    bins = []

    for item in items:
        # Пытаемся поместить предмет в существующий ящик
        placed = False
        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                placed = True
                break
        # Если предмет не поместился ни в один ящик, создаем новый ящик
        if not placed:
            bins.append(item)

    return len(bins), bins

# Пример использования
items = [4, 8, 1, 4, 2, 1]  # Размеры предметов
bin_capacity = 10            # Вместимость ящика

num_bins, bins = bin_packing(items, bin_capacity)
print(f"Количество использованных ящиков: {num_bins}")
print(f"Оставшаяся вместимость ящиков: {bins}")
