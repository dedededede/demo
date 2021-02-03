# -*- encoding: utf8 -*-
a = [4, 5, 6, 3, 2,1, 0]
for index1 in range(1, len(a)):
    value = a[index1]
    while index1 - 1 >= 0:
        if a[index1 - 1] > value:
            a[index1] = a[index1 - 1]
        else:
            break
        index1 -= 1
    a[index1] = value


print a







