from ParameterConstructorImpl import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self,a,b):
       Calculator.__init__(self,a,b)


    def getCompleteData(self):
        return ChildImpl.num2 + self.Additiona()


# Throws error
child1 = ChildImpl()
child1.getCompleteData()

# Hence We have to pass the variables which parant class constructor has

child = ChildImpl(20, 30)
vars = child.getCompleteData()
print(vars)
