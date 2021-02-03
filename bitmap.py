class BitMap(object):
    def __init__(self, nbits):
        self.nbits = nbits
        self.bytes = [0 for i in range(nbits + 1)]

    def set(self, k):
        if k > self.nbits:
            return
        byteIndex = k / 64
        bitIndex = k % 64
        self.bytes[byteIndex] |= (1 << bitIndex)

    def get(self, k):
        if k > self.nbits:
            return False
        byteIndex = k / 64
        bitIndex = k % 64
        return self.bytes[byteIndex] & (1 << bitIndex) != 0

obj = BitMap(100)
print obj.bytes
for i in range(100):
    obj.set(i)
print obj.bytes
for i in range(1000):
    print i, obj.get(i)