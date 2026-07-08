def Add(No1, No2):
    return No1+No2
    
def main():

    Value1 = int(input("Enter First number : "))
    Value2 = int(input("Enter Second number : "))

    Ret = Add(Value1, Value2)
    print("Addition of Numbers is : ",Ret)

if __name__ =="__main__":
    main()