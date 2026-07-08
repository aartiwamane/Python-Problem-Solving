
def CalculateFreq(List1, Value):
    Count = 0
    for i in List1:
        if(i == Value):
            Count = Count+1

    return Count

def main():
    Data = list()
    No1 = int(input("Enter the number of Elements want to enter in a list : "))
    
    for i in range(No1):
        Values = int(input(f"Enter {i} th Element of List : "))
        Data.append(Values)

    No2 = int(input("Enter the Elemets to be Search : "))
    Ret = CalculateFreq(Data, No2)

    print(f"The Frequency of {No2} Element in list is : ",Ret)

if __name__ == "__main__":
    main()