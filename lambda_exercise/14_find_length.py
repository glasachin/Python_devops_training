# Write a Python program to find the values of length six in a given list using Lambda
# Sample Output:
# Monday
# Friday
# Sunday

a = ['sunday','monday','tuesday','wednesday','thurshday','friday','saturday','January','february','march','april']

b = lambda x: [i for i in x if len(i) == 6]

print("List with length of 6: \n",b(a))

# ---------other solution-------------
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)