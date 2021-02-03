def count_sort(data, length):
    max = data[0]
    for i in range(1, length):
        if max < data[i]:
            max = data[i]
    new_data = [0 for i in range(max+1)]
    for index, i in enumerate(data):
        new_data[i] += 1

    for i in range(1, len(new_data)):
        new_data[i] = new_data[i-1] + new_data[i]

    result = [None for i in range(length)]
    for i in range(length - 1, -1, -1):
        item = data[i]
        result[new_data[item] - 1] = item
        new_data[item] -= 1

    return result

data = [2, 5, 3, 0, 2, 3, 0, 3]
count_sort(data, len(data))