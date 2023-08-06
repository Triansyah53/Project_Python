class myclass1:
    def __init__(self,cls1_input_1):
        print('init of class 1')
        self.prop_cls1=10
        self.cl1_in_1=cls1_input_1
        print(self.cl1_in_1)

    def method_1_class_1(self):
        print('method_1_class_1')

# obj1=myclass1()
# obj1.method_1_class_1()

class myclass2(myclass1):
    def __init__(self,cl1in1,cl1in2):
        super().__init__(cl1in1)
        print('init of class 2')
        self.cl1in2=cl1in2

    def method_1_class_2(self):
        print('method_1_class_2')


obj2=myclass2('abc','bca')
# obj2.method_1_class_2()
print(obj2.cl1_in_1)