# -*- encoding: utf8 -*-
import threading
from threading import Semaphore
class H2O:
    def __init__(self):
        self.s1,self.s2 = Semaphore(2), Semaphore(1)
        self.H, self.O = 0, 0

    def hydrogen(self, releaseHydrogen):
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.s1.acquire()
        releaseHydrogen()
        self.H += 1
        if self.O == 1 and self.H == 2:
            self.H,self.O = 0,0
            self.s1.release()
            self.s1.release()
            self.s2.release()

    def oxygen(self, releaseOxygen):
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.s2.acquire()
        releaseOxygen()
        self.O += 1
        if self.O == 1 and self.H == 2:
            self.H,self.O = 0,0
            self.s1.release()
            self.s1.release()
            self.s2.release()



obj = H2O("HH0HH0")
thread1 = threading.Thread(target=obj.hydrogen, args=('zero', ))
thread2 = threading.Thread(target=obj.oxygen, args=('even', ))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
