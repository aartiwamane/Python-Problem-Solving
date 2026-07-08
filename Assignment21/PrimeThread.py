import threading

def ChkPrime(No):
    if (No<=1):
        return False
    
    for i  in range(2,No):
        if(No%i == 0):
            return False
        
    return True

def PrimeNum(Data1):
    print("Prime Numbers from List are :")
    for num in Data1:
        Res = ChkPrime(num)
        if Res:
            print(num)

def NonPrimeNum(Data1):
    print("Non-Prime Numbers from List are :")
    for num in Data1:
        Res = ChkPrime(num)
        if(Res == True):
            pass
        else:
            print(num)

def main():
    Data = list()

    Num = int(input("Enter the number of Elements of List : "))

    for i in range(Num):
        Value = int(input(f"Enter the {i} th Element of List : "))
        Data.append(Value)
    

    t1 = threading.Thread(target=PrimeNum,args=(Data,))
    t2 = threading.Thread(target=NonPrimeNum,args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()