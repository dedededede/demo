a = [1, 2, 3, 3]

count_xor = 0
for i in a:
    count_xor ^= i

for j in range(32):
    if (count_xor >> j) & 1 == 1:
        break

list1, list2 = [], []
for i in a:
    if (i >> j) & 1 == 1:
        list1.append(i)
    else:
        list2.append(i)

print 2 * sum(set(list1)) - sum(list1)
print 2 * sum(set(list2)) - sum(list2)

###

###

