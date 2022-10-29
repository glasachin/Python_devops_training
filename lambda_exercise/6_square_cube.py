a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = lambda x:x**2
c = lambda x:x**3

b = [s(x) for x in a]
d = [c(x) for x in a]

print('Squares: ', b)
print('Cube: ',d)