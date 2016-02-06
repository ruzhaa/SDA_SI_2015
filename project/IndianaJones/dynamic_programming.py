def knapsack_problem_dp(limit, items):

    # 1) create table only with 0
    # 2) generation table with new value from tuple_of_items
    # * items[j-1] -> item, weight, val (from tuple)

    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, weight, val = items[j-1]
        for w in range(1, limit + 1):
            if weight > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w], val + table[j-1][w-weight])

    result = []

    for j in range(len(items), 0, -1):
        # return in the previous row
        if table[j][limit] != table[j-1][limit]:
            item, weight, val = items[j-1]
            result.append(items[j-1])
            limit -= weight

    return result
