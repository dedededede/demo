# -*- encoding: utf8 -*-
a = [4, 5, 6, 3, 2, 1]
count = 0
for index1 in range(len(a)):
    for index2 in range(index1 + 1, len(a)):
        if a[index1] > a[index2]:
            count += 1
            temp = a[index2]
            a[index2] = a[index1]
            a[index1] = temp

print a, count


