# Write a Python program to add two given lists using map and lambda.
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]

a = [1,2,3]
b = [4,5,6]

c = map(lambda x,y:x+y, a,b)
# print(c)
# for i in c:
#     print(i)
print(list(c)) #once we read the elements, it becomes empty
print(list(c))