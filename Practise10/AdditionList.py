
def AddList(List1):
    Sum = 0
    for i in List1:
        Sum = Sum+i

    return Sum

def main():
    Data = list()
    No1 = int(input("Enter the number of Elements want to enter in a list : "))

    for i in range(No1):
        Values = int(input(f"Enter {i} th Element of List : "))
        Data.append(Values)


    Ret = AddList(Data)
    print("Addition of Elements from List: ",Ret)

if __name__ == "__main__":
    main()