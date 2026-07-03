def EvenNum(No):
        Num = list()
        i = 0
        while(i<=No):
            if((i%2) != 0):
                Num.append(i)
            i = i+1
        return Num
         
def main():
    Value = int(input("Enter the number : "))

    Ret = EvenNum(Value)
    print(Ret)


if __name__ == "__main__":
    main()