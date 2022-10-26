# sort the list of dictionary based on model number
a = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'shoppingmode Samsung', 'model': 7, 'color': 'Blue'}]

a.sort(key = lambda x: x['color'])
print(a)

# using 'sorted'
b = sorted(a, key = lambda x: x['color'])
print('Using Sorted: ',b)
