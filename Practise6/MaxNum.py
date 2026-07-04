
FindMax = lambda Value1,Value2:(Value1 > Value2)
        
def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    Ret = FindMax(No1,No2)
    if Ret:
        print("This is Maximaum number :",No1)
    else:
        print("This is Maximu  Number : ",No2)

if __name__ == "__main__":
    main()