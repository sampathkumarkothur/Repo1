clas Test:
    a=10
    def __init__(self):
        print(Test.a)
        print(self.a)
    def m1(self):
        print("Inside instance method")
        print(Test.a)
        print(self.a)

    @classmethod
    def m2(cls):
        print("Inside class method")
        print(Test.a)
        print(cls.a)

    @staticmethod
    def m3():
        print("Inside Static method")
        print(Test.a)
        print()

t=Test()
t.a=10
Test.a=20
