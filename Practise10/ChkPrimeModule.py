from MarvellousNum import *

def main():
    Data = list()
    No1 = int(input("Enter the number of Elements want to enter in a list : "))

    for i in range(No1):
        Values = int(input(f"Enter {i} th Element of List : "))
        Data.append(Values)

    Ret = list()

    for no in Data:
        if ChkPrime(no):
            Ret.append(no)
        else:
            print(f"{no} is not a Prime Number..")

    sum = 0
    for i in Ret:
        sum = sum+i

    print(f"Prime Numbers From List are :{Ret}")
    print(f"Addition of all Prime numbers form List are : {sum})

if __name__ == "__main__":
    main()
