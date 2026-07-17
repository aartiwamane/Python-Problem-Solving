class Arithmetic():

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the First Number : "))
        self.Value2 = int(input("Enter the Second Number  : "))
   
    def Addition(self):
        return self.Value1+self.Value2
    
    def Substraction(self):
        return self.Value1-self.Value2
    
    def Multiplication(self):
        return self.Value1*self.Value2
    
    def Division(self):
        try:
            return self.Value1/self.Value2
    
        except ZeroDivisionError as zobj:
            print(f"Exception Occured due to Second Paramter is Zero")

obj1 = Arithmetic()

Result1 = obj1.Accept()
    
Result2 = obj1.Addition()
print(f"Addition of Accepted Input Variables are : {Result2}")

Result3 = obj1.Substraction()
print(f"Substraction of Accepted Input Variables are : {Result3}")

Result4 = obj1.Multiplication()
print(f"Multiplication of Accepted Input Variables are : {Result4}")

Result5 = obj1.Division()
print(f"Division of Accepted Input Variables are : {Result5}")

obj2 = Arithmetic()

Result1 = obj2.Accept()
    
Result2 = obj2.Addition()
print(f"Addition of Accepted Input Variables are : {Result2}")

Result3 = obj2.Substraction()
print(f"Substraction of Accepted Input Variables are : {Result3}")

Result4 = obj2.Multiplication()
print(f"Multiplication of Accepted Input Variables are : {Result4}")

Result5 = obj2.Division()
print(f"Division of Accepted Input Variables are : {Result5}")