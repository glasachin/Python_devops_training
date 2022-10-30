
# check = lambda x: True if x.isdigit() else False
check = lambda x: x.replace('.','').isdigit()
print(check('3asf'))