def mul(n):
    return lambda x : x*n

r = mul(5)
print(r(3))