import threading

def EvenList(Data1):
    Sum = 0
    for i in Data1:
        if(i%2 == 0):
            Sum = Sum+i

    print(f"Sum of Even Numbers from List is {Sum}")

def OddList(Data1):
    Sum = 0
    for i in Data1:
        if(i%2 != 0):
            Sum = Sum +i
    print(f"Sum of Odd Numbers from List is {Sum}")

def main():
    Data = list()

    Value = int(input("Enter the number of  elements in a list : "))

    for i in range(Value):
        Num = int(input(f"Enter the {i} th Element in a list : "))
        Data.append(Num)

    t1 = threading.Thread(target=EvenList,args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()