def ChkDivisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():

    Value = int(input("Enter a number : "))

    Ret = ChkDivisible(Value)
    
    if Ret:
        print("Number is Divisible by Five..")
    else:
        print("Number is Not Divisible by Five...")

if __name__ =="__main__":
    main()