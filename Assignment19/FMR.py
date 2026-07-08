from functools import reduce

def ChkNums(No1):
    if(No1>=70 and No1<=90):
        return No1

def Increment(No):
    return No+10

def ProductAll(No,No1):
    return No*No1

def main():
    Data = list()

    Num = int(input("Enter the number of elements in list : "))

    for i in range(Num):
        Value = int(input(f"Enter the {i} th element of list : "))
        Data.append(Value)

    print(f"Input list is : {Data}")

    FData = list(filter(ChkNums,Data))
    print(f"Data after filter function: {FData}")

    MData = list(map(Increment,FData))
    print(f"Data after Map function : {MData}")

    RData = reduce(ProductAll,MData)
    print(f"Data aftre Reduce : {RData}")


if __name__ == "__main__":
    main()