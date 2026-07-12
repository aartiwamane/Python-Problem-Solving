import multiprocessing
import os
import time

def EvenSumCalculate(No):
    print(f"PID of the Factorial Function process is : {os.getpid()}")
    
    Sum = 0
    for i in range(1,No+1):
        if (i % 2 == 0):
            Sum = Sum+i
       
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

    result = P.map(EvenSumCalculate,Data)
    P.close()
    P.join()
    end_time = time.perf_counter()

    print(f"Summation of Even Numbers from input Data is : {result}")
    print(f"Time Required is : {end_time-start_time:.4f}")


if __name__ == "__main__":
    main()