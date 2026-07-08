import threading

Product = 1
Sum = 0
def SumList(Data1):
    global Sum
    for i in Data1:
        Sum = Sum+i

def ProductList(Data1):
    global Product
    for num in Data1:
        Product = Product*num

def main():
    Data = list()

    global Sum
    global Product

    Num = int(input("Enter the number of Elements of List : "))

    for i in range(Num):
        Value = int(input(f"Enter the {i} th Element of List : "))
        Data.append(Value)

    t1 = threading.Thread(target=SumList,args=(Data,))
    t2 = threading.Thread(target=ProductList,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print(f"Sum of all Elements from List : {Sum}")
    print(f"Product of all Elements from List :{Product}")

if __name__ == "__main__":
    main()