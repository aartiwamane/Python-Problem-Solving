
ChkOdd = lambda Value1:(Value1 % 2 != 0)
        
def main():
    No1 = int(input("Enter First Number :"))
    

    Ret = ChkOdd(No1)
    if Ret:
        print("The Number is Odd Number..")
    else:
        print("The Number is Even Number...")

if __name__ == "__main__":
    main()