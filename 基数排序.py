a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
x = a[0]
for i in a[1:]:
    if i > x:
        x = i
bucket = [[] for i in range(10)]

def get_pos(data, pos):
    if pos == 0:
        return data % 10
    else:
        return data / (pos * 10) % 10

for i in range(len(str(x))):
    for j in a:
        index = get_pos(j, i)
        bucket[index].append(j)

    a = []
    for i in bucket:
        a.extend(i)
    bucket = [[] for i in range(10)]
print a


