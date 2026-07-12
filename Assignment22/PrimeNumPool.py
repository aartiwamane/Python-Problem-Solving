import multiprocessing
import os

def PrimeNum(No):
    if No <= 1:
        return False
    
    for i in range(2,No):
        if (No % i== 0):
            return False
    return True

def PrimNumCalculate(No):
    print(f"PID of the Factorial Function process is : {os.getpid()}")
    
    prime = 1

    for i in range(1,No+1):
        res = PrimeNum(i)
        if res:
            prime  = prime+1
    return prime

def main():
    print(f"PID of main Process is : {os.getpid()}")

    Data = list()
    No1 = int(input("Enter the number of elements to be entered : "))

    for i in range(No1):
        Values = int(input(f"Enter the {i} th Element of List :"))
        Data.append(Values)
        
    print(f"Input Data is : {Data}")

    result = []

    P = multiprocessing.Pool()
    result = P.map(PrimNumCalculate,Data)
    P.close()
    P.join()
    print(f"Prime Numbers count from the input Data is : {result}")


if __name__ == "__main__":
    main()