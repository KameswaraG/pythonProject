class Calculator:
    sum = 200

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def firstMehtod(self):
        print("This is a method")

    def Additiona(self):
        return self.firstNumber+self.secondNumber+Calculator.sum


calc=Calculator(10,15)
calc.firstMehtod()
print(calc.Additiona())


calc2=Calculator(25,10.5)
print(calc2.Additiona())
