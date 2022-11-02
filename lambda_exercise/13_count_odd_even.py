# Write a Python program to count the even, odd numbers in a given array of integers using Lambda. 
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

a = [1, 2, 3, 5, 7, 8, 9, 10]

odd_num = lambda x: len([i for i in x if i%2 != 0])
even_num = lambda x: len([i for i in x if i%2 == 0])

print('Odd num: ', odd_num(a))
print('Even num: ', even_num(a))

# ---------Othe solution---------------
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)
