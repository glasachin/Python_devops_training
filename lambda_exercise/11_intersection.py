# Write a Python program to find intersection of two given arrays using Lambda
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

intersection = lambda x,y: [i for i in x if i in y]

a = [1,3,4,5]
b = [1,3,7,10,3,5,6,0]

print(intersection(a,b))

# ------------another method using filter--------------
result = list(filter(lambda x: x in a, b)) 
print('using filter: ',result)