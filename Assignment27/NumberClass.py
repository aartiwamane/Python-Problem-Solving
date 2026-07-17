class Numbers():

    def __init__(self,Value):
        self.Value=Value

    def ChkPrime(self):
        if self.Value<=0:
            return False
        
        for i in range(2,self.Value):
            if self.Value%i == 0:
                return False   
        return True
    
    def ChkPerfect(self):
        Sum = 0
        
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                Sum = Sum+i
        return Sum == self.Value
        
    def Factors(self):
        fact = list()

        for i in range(1,self.Value+1):
            if self.Value%i == 0:
                fact.append(i)
        return fact
    
    def SumFactors(self):
        Data = self.Factors()
        Sum = 0

        for i in Data:
            Sum = Sum+i
        return Sum

Num1 = int(input(f"Enter the number :"))

obj1 = Numbers(Num1)

Ret = obj1.ChkPrime()
if Ret:
    print(f"Number is Prime Number...")
else:
    print(f"Number is not a prime Number...")

Ret1 = obj1.ChkPerfect()
if Ret1:
    print(f"Number is Perfect Number...")
else:
    print(f"Number is not Perfect..")

Ret2 = obj1.Factors()
print(f"Factors of the number are : {Ret2}")

Ret3 = obj1.SumFactors()
print(f"Sum of the all Factors of Number is : {Ret3}")

Num2 = int(input(f"Enter the number :"))

obj2 = Numbers(Num2)

Ret = obj2.ChkPrime()
if Ret:
    print(f"Number is Prime Number...")
else:
    print(f"Number is not a prime Number...")

Ret1 = obj2.ChkPerfect()
if Ret1:
    print(f"Number is Perfect Number...")
else:
    print(f"Number is not Perfect..")

Ret2 = obj2.Factors()
print(f"Factors of the number are : {Ret2}")

Ret3 = obj2.SumFactors()
print(f"Sum of the all Factors of Number is : {Ret3}")