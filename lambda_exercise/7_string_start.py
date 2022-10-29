a = 'Hi, This is Sachin!'
b = 'Hi'
c = lambda x,y: True if x.startswith(y) else False

print(c(a,b))