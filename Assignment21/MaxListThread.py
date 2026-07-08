import threading

def ChkMax(Data1):
    Max = Data1[0]
    for num in Data1:
       if(num>Max):
           Max = num
    print(f"Maximum Element of List : {Max}")

def ChkMin(Data1):
    Min = Data1[0]
    for num in Data1:
        if(num<Min):
            Min = num
    print(f"Minimum Element from List : {Min}")

def main():
    Data = list()

    Num = int(input("Enter the number of Elements of List : "))

    for i in range(Num):
        Value = int(input(f"Enter the {i} th Element of List : "))
        Data.append(Value)

    t1 = threading.Thread(target=ChkMax,args=(Data,))
    t2 = threading.Thread(target=ChkMin,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()