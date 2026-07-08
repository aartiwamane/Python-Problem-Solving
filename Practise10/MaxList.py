
def AddList(List1):
    Max = List1[0]
    for i in List1:
        if(i>Max):
            Max=i

    return Max

def main():
    Data = list()
    No1 = int(input("Enter the number of Elements want to enter in a list : "))

    for i in range(No1):
        Values = int(input(f"Enter {i} th Element of List : "))
        Data.append(Values)


    Ret = AddList(Data)
    print("Maximum Element from List is : ",Ret)

if __name__ == "__main__":
    main()