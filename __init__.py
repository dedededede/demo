from random import randint
import array
from memory_profiler import profile
b = [randint(1, 1000) for i in range(10)]


def testa(b):
    mysql_dict = {}
    for item in b:
        if item in mysql_dict:
            mysql_dict[item] += 1
        else:
            mysql_dict[item] = 1

    result = []
    for item in mysql_dict:
        if mysql_dict[item] == 1:
            result.append(item)


def testb(b):
    length = max(max(b), len(b))
    dest_list = [0 for i in xrange(length + 1)]
    for i in b:
        dest_list[i] += 1

    result = []
    for index, i in enumerate(dest_list):
        if i == 1:
            result.append(index)


from bitmap import BitMap
bm = BitMap(32)
print bm.tostring()
bm.set(21)

print bm.tostring()

from array import array
array.fromfile()


from cli import lock


