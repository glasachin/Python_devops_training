a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ev = list(filter(lambda x: x%2 == 0, a))
print('Even Numbers: ',ev)

odd = list(filter(lambda x: x%2 != 0, a))
print('odd Numbers: ', odd)
