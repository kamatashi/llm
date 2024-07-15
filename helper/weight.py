def weighted_average(items, index=0, sum_weight=0, weighted_sum=0):
    if index >= len(items):
        return weighted_sum / sum_weight

    item = items[index]
    return weighted_average(
        items,
        index + 1,
        sum_weight + item['weight'],
        weighted_sum + item['level'] * item['weight']
    )

# Exemplo de uso com uma lista de itens
items = [{'level': 10, 'weight': 2}, {'level': 20, 'weight': 3}, {'level': 30, 'weight': 4}]
print(weighted_average(items))
