
def MinCalculate(List1):
    Min = List1[0]
    for i in List1:
        if(i<Min):
            Min=i

    return Min

def main():
    Data = list()
    No1 = int(input("Enter the number of Elements want to enter in a list : "))
    
    for i in range(No1):
        Values = int(input(f"Enter {i} th Element of List : "))
        Data.append(Values)


    Ret = MinCalculate(Data)
    print("Minimum Element from List is : ",Ret)

if __name__ == "__main__":
    main()