
Multiplication =  lambda Value1,Value2 : Value1*Value2

def main():
    No1 = int(input("Enter First number : "))
    No2 = int(input("Enter Second Number : "))

    Ret = Multiplication(No1,No2)
    print("Multiplication is : ",Ret)
    
if __name__ == "__main__":
    main()