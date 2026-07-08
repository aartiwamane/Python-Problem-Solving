import threading

def EvenFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if(No%i == 0):
            if(i % 2 == 0):
                Sum = Sum+i

    print(f"Sum of Even Fators of {No} is {Sum}")

def OddFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if(No%i == 0):
            if(i%2 != 0):
                Sum = Sum +i
    print(f"Sum of Odd Fators of {No} is {Sum}")

def main():
    

    t1 = threading.Thread(target=EvenFactor,args=(48,))
    t2 = threading.Thread(target=OddFactor, args=(48,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main Thread..")
if __name__ == "__main__":
    main()