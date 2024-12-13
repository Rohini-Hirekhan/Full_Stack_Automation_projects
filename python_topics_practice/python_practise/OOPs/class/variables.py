class Demo_class:
    static_variable1 ="rohini"

    def __init__(self):
        self.instance_variable1=30
        print("instance variable1",self.instance_variable1)
        Demo_class.static_variable2="rushi"
        print("print static value of constructor",self.static_variable1)
        print("print static value of constructor", Demo_class.static_variable2)

    def instance_method(self):
        x=12 #local variable
        self.insinstance_variable2 =89
        print("insinstance_variable2", self.insinstance_variable2 )
        Demo_class.static_variable3 = "M"
        print("print static value of instance method", Demo_class.static_variable3)

    @staticmethod
    def static_method(self,cls):
        y=13 #local variable
        cls.mi="ghj"
        Demo_class.static_variable3=" v"
        print("print static value of instance method", Demo_class.static_variable2)
        print("print static value of static method using class name", Demo_class.static_variable3)
        print("print static value of static method using self name", self.static_variable3)


    @classmethod
    def class_method(self,cls):
        z=14
        cls.static4 = "mk"
        Demo_class.static5="nj"
        print("print static value from class variable",Demo_class.static5)
        print()
        self.er=56


obj=Demo_class()
obj.instance_variable3 = 20
obj.static_variable = 56
print("instance_variable3 ", obj.instance_variable3)
obj.instance_method()
obj.static_method()
obj.mi