
class demo():
    def __init__(self, l):
        self.list_ = l
    
    def appendList(self, data):
        self.list_.append(data)

    def displayList(self):
        print(self.list_)


a = []
print('a: ', a)
b = demo(a)

b.appendList(10)
b.displayList()
print('a: ', a)

b.appendList(10)
print('a: ', a)

a.append(40)
print('b: ')
b.displayList()