
FindMin = lambda Value1,Value2:(Value1 > Value2)
        
def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    Ret = FindMin(No1,No2)
    if Ret:
        print("This is Minimum number :",No2)
    else:
        print("This is Minimum  Number : ",No1)

if __name__ == "__main__":
    main()