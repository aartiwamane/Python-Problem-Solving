def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():

    Value = int(input("Enter a number : "))

    Ret = ChkNum(Value)
    
    if Ret:
        print("Number is Even Number..")
    else:
        print("Number is Odd Number...")

if __name__ =="__main__":
    main()