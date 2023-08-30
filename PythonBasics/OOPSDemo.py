# Classes are used to define a prototype
# Classes contains variables, Methods, instance variables & constructor

class Calculator:
    num=100

    #Constructor creation
    def __init__(self):
        print("I am called when object created")



    def getData(self):
        print("I am executiong a method in a class")

# Object creation
obj=Calculator()
obj.getData()
print(obj.num)