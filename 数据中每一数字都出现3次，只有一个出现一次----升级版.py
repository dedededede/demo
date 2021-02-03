a = [8, 8, 7, 7, 10]
size = 32
c = [0 for i in range(32)]
count = 2

for i in a[:]:
    for j in range(32):
        c[j] += (i >> j) & 1


result = [0 for i in range(32)]
for i in range(len(c)):
    if c[i] % count != 0:
        result[i] += c[i] % count

temp = 0
for i in range(len(result)):

    if result[i] == 0:
        continue
    else:
        temp += 2 ** i

print temp
