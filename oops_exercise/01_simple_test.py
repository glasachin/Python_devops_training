class student:
    var = 'This is created by sachin'
    def __init__(self,a,b):
        self.a = a
        self.b = b 
    def sum(self):
        return self.a+self.b

class st(student):

    def sub(self):
        return self.a - self.b

test = student(10,13)
print(test.var,test.a,test.b,test.sum())

test1 = st(10,13)
print(test1.var,test1.a,test1.b,test1.sum(),test1.sub())