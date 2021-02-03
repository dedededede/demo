a = [4,5,6,5,6,7,8,9,10,9,10]
def find_num(list, n, num):
    next_index = abs(num - list[0])
    result = []
    while next_index < n:
        if list[next_index] == num:
            result.append(next_index)
            next_index += 2
        else:
            next_index += abs(num - list[next_index])
    return result

print find_num(a, len(a), 10)
