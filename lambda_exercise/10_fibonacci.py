# This file generates n digits of fibonacci series using lambda

from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

print(fib_series(3))