def f(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    return f(n - 1) + f(n - 2)

def f1(n):
    a = 0
    b = 1
    for i in xrange(n):
        b, a = a + b, b

    return b

def f2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


for n in f2(5):
    print n