def ChkPositiveNegative(No):
    if(No == 0):
        print("Zero")
    elif(No>=1):
        print("Positive Number..")
    else:
        print("Negative Number..")

def main():

    Value = int(input("Enter a number : "))

    ChkPositiveNegative(Value)
    
    
if __name__ =="__main__":
    main()