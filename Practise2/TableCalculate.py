def CalculateTable(No):
    Table = []

    for i in range(1,11):
        Table.append(i*No)
    return Table

    

def main():
    Value = int(input("Enter the number to calculate Table : "))

    Ret = CalculateTable(Value)
    print(Ret)
    

if __name__ == "__main__":
    main()