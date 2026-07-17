class Circle():
    #class variable
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.cicumference = 0.0

    def Accept(self):
        self.radius = int(input("Enter the radius of circle : "))

    def CalculateArea(self):
        self.area = self.PI*self.radius*self.radius

    def CalculateCircumference(self):
        self.cicumference = 2*self.PI*self.radius

    def Display(self):
        print("Radisu of Circle is : ",self.radius)
        print(f"Area of circle is : {self.area}")
        print(f"Circumference of Circle is : {self.cicumference}")

obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()