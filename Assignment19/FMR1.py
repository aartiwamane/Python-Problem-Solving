from functools import reduce

ChkEven  = lambda No1: (No1%2==0)

Square = lambda No : No*No

SumAll = lambda No,No1: No+No1

def main():
    Data = list()

    Num = int(input("Enter the number of elements in list : "))

    for i in range(Num):
        Value = int(input(f"Enter the {i} th element of list : "))
        Data.append(Value)

    print(f"Input list is : {Data}")

    FData = list(filter(ChkEven,Data))
    print(f"Data after filter function: {FData}")

    MData = list(map(Square,FData))
    print(f"Data after Map function : {MData}")

    RData = reduce(SumAll,MData)
    print(f"Data aftre Reduce : {RData}")


if __name__ == "__main__":
    main()