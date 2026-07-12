import multiprocessing
import os

def SquareCalculate(No):
    Sum = 0
    for i in range(No):
        Sum = Sum+(i*i)
    return Sum

def main():
    Data = list()
    No1 = int(input("Enter the number of elements to be entered : "))

    for i in range(No1):
        Values = int(input(f"Enter the {i} th Element of List :"))
        Data.append(Values)
        
    print(f"Input Data is : {Data}")

    result = []

    P = multiprocessing.Pool()
    result = P.map(SquareCalculate,Data)
    P.close()
    P.join()
    print(f"Result of the input Data is : {result}")


if __name__ == "__main__":
    main()