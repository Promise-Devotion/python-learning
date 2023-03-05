# 字典增加属性
tel = {'jack': 4098, 'sape': 4139}
tel['jim'] = 5000

print(tel['jack'])
# 删除属性
del tel['jim']
print(list(tel))

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
result = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(result)
# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
print({x: x**2 for x in (2, 4, 6)})
# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
print(dict(sape=4139, guido=4127, jack=4098))