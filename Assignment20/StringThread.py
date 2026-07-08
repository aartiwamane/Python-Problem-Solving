import threading

def SmallCaseLetters(Data1):
    print(f"Thread Id of SmallCaseLetters Thread is : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

    count = 0

    for ch in Data1:
        if(ch >= 'a' and ch <='z'):
            count = count+1

    print(f"Count of Small Case Characters in {Data1} is {count}")

def UpperCaseLetters(Data1):
    print(f"Thread Id of UpperCaseLetters Thread is : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

    Count = 0

    for ch in Data1:
        if(ch >= 'A' and ch <= 'Z'):
            Count = Count+1

    print(f"Count of Upper Case Characters in {Data1} is {Count}")

def Digits(Data1):
    print(f"Thread Id of Digits Thread is : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

    Count = 0

    for i in Data1:
        if( i>='0' and i<='9'):
            Count = Count+1

    print(f"Count of Digits fro {Data1} is {Count}")

def main():
    print(f"Thread Id of Main Thread is : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    Data = "AartiWamane2204"

    t1 = threading.Thread(target=SmallCaseLetters,args=(Data,))
    t2 = threading.Thread(target=UpperCaseLetters, args=(Data,))
    t3 = threading.Thread(target=Digits,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

if __name__ == "__main__":
    main()