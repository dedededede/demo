# -*- encoding: utf8 -*-
import threading
import time
semaphore = threading.BoundedSemaphore(1)
def run(n):
   # semaphore.acquire()  #信号量获取一把锁
   # time.sleep(1)
   # print("run the thread: %s" % n)
   # semaphore.release()
   with semaphore:
       time.sleep(1)
       print("run the thread: %s" % n)

for i in range(20):
      t = threading.Thread(target=run, args=(i,))
      t.start()

while threading.active_count() != 1:
    print "activeCunt:", threading.active_count()

