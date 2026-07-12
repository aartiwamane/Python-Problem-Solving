import multiprocessing
import os
import time

def MultipleCalculate(No):
    print(f"PID of the Factorial Function process is : {os.getpid()}")
    Multiple = 1
    Sum = 0
    for i in range(1,No+1):
        Multiple = i**5
        Sum = Sum+Multiple
    return Sum

def main():
    print(f"PID of main Process is : {os.getpid()}")

    Data = list()
    No1 = int(input("Enter the number of elements to be entered : "))

    for i in range(No1):
        Values = int(input(f"Enter the {i} th Element of List :"))
        Data.append(Values)
        
    print(f"Input Data is : {Data}")

    result = []
    
    start_time = time.perf_counter()

    P = multiprocessing.Pool()
    #print("CPU Count : ",multiprocessing.cpu_count())

    result = P.map(MultipleCalculate,Data)
    P.close()
    P.join()
    end_time = time.perf_counter()

    print(f"Summation of Multiple of five of the input Data is : {result}")
    print(f"Time Required is : {end_time-start_time:.4f}")


if __name__ == "__main__":
    main()