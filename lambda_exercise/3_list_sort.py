# Sort this list in ascending order of numbers using lambda function
a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# r = lambda x: [i[1] for i in x]
# s = lambda x: r(x).sort()
a.sort(key = lambda x: x[1])

print(a)