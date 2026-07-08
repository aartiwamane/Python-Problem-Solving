import threading

Count = 0
lock = threading.Lock()

def Increment():
    global Count

    for i in range(10000):
        lock.acquire()
        Count = Count+1
        lock.release()

def main():
    global Count

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Count : ",Count)
if __name__ == "__main__":
    main()