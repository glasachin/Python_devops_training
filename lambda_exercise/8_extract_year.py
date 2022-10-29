a = '2020-01-15 09:03:32.744178'
year = lambda x: x.split(' ')[0].split('-')[0]
month = lambda x: x.split(' ')[0].split('-')[1]
date = lambda x: x.split(' ')[0].split('-')[2]

print('Year: ', year(a))
print('month: ', month(a))
print('date: ', date(a))
