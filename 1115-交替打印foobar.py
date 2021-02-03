import threading
from threading import Lock
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            if self.foo_lock.acquire():
                printFoo()
                self.bar_lock.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            if self.bar_lock.acquire():
                printBar()
                self.foo_lock.release()

obj = FooBar(10)

thread1 = threading.Thread(target=obj.foo, args=('foo', ))
thread2 = threading.Thread(target=obj.bar, args=('bar', ))

thread1.start()
thread2.start()