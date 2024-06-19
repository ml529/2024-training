import threading

def job1():
    global A ,lock
    lock.acquire()
    for i in range(10):
        A +=1
        print(f"job1 {A}")
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A +=10
        print(f"job2 {A}")
    lock.release()

A = 0
lock = threading.Lock()
t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start()
t2.start()
t1.join()
t2.join()