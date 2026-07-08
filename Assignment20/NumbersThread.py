import threading

def DisplayNumbers(No):
    print("First 50 numbers : ")
    for i in range(1,No+1):
        print(i)

def DisplayReverse(No):
    print("Numbers in Reverse Order : ")
    for i in range(50,0,-1):
        print(i)

def main():
    
    t1 = threading.Thread(target=DisplayNumbers,args=(50,))
    t2 = threading.Thread(target=DisplayReverse,args=(50,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()