import threading
from threading import Lock
class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.fizz_lock = Lock()
        self.fizz_lock.acquire()

        self.buzz_lock = Lock()
        self.buzz_lock.acquire()

        self.fizzbuzz_lock = Lock()
        self.fizzbuzz_lock.acquire()

        self.number_lock = Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.fizz_lock.acquire()
                printFizz()
                self.number_lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n + 1 ):
            if i % 5 == 0 and i % 3 != 0:
                self.buzz_lock.acquire()
                printBuzz()
                self.number_lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzz_lock.acquire()
                printFizzBuzz()
                self.number_lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.number_lock.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzz_lock.release()
            elif i % 3 == 0 and i % 5 != 0:
                self.fizz_lock.release()
            elif i % 5 == 0 and i % 3 != 0:
                self.buzz_lock.release()
            else:
                printNumber(i)
                self.number_lock.release()


obj = FizzBuzz(100)
thread1 = threading.Thread(target=obj.fizz, args=('zero', ))
thread2 = threading.Thread(target=obj.buzz, args=('even', ))
thread3 = threading.Thread(target=obj.fizzbuzz, args=('even', ))
thread4 = threading.Thread(target=obj.number, args=('even', ))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

