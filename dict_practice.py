a = {}
a['apple'] = 'fruit'
a['celery'] = 'vegetable'
a['banana'] = 'fruit'
a['apple'] = 'vegetable'
del a['banana']
for key, value in a.items():
    print(key, value)

for key in a.iterkeys():
    print(key)
