spam = {
    'firstName': 'Kenneth',
    'secondName': 'Alvares',
    'age': 23,
    'height': 186,
    'weight': 72,
    'country': 'India',
    'favoriteColor': 'red'
    }

print('Printing .values()')
for v in spam.values():
    print(v)
print()

print('Printing .keys()')
for k in spam.keys():
    print(k)
print()

print('Printing .items()')
for i in spam.items():
    print(i)
