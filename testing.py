# ThreadTest01.py - Demonstrates that if non-atomic actions on
# global variables are protected, task can intrude on each other.
from threading import Thread
import time

# global variable
a = 0; NN = 100

def thread1(threadname):
    while True:
      if a % 2 and not a % 2:
          print("unreachable.")
    # end of thread1

def thread2(threadname):
    global a
    for _ in range(NN):
        a += 1
        time.sleep(0.1)
    # end of thread2

thread1 = Thread(target=thread1, args=("Thread1",))
thread2 = Thread(target=thread2, args=("Thread2",))

thread1.start()
thread2.start()

thread2.join()
# end of ThreadTest01.py