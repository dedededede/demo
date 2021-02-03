# -*- encoding: utf8 -*-
a = [3, 2, 1, 0]
for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print a
