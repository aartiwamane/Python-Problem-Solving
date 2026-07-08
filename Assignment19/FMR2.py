from functools import reduce

def PrimeNum(No1):
    if(No1 <= 1):
        return False

    for i in range(2,No1):
        if(No1%i == 0):
            return False
        
    return True

def MultiplyByTwo(No):
    return No*2

def MaxNum(No,No1):
    if(No>No1):
        return No
    else:
        return No1

def main():
    Data = list()

    Num = int(input("Enter the number of elements in list : "))

    for i in range(Num):
        Value = int(input(f"Enter the {i} th element of list : "))
        Data.append(Value)

    print(f"Input list is : {Data}")

    FData = list(filter(PrimeNum,Data))
    print(f"Data after filter function: {FData}")

    MData = list(map(MultiplyByTwo,FData))
    print(f"Data after Map function : {MData}")

    RData = reduce(MaxNum,MData)
    print(f"Data aftre Reduce : {RData}")


if __name__ == "__main__":
    main()