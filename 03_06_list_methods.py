# List methods
pets = ['dog', 'cat', 'moose']

print('pets = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')

print('pets.index(\'cat\') = ' + str(pets.index('cat')))

pets.append('fish')

print('pets.append(\'fish\') = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')

pets.insert(1, 'chicken')

print('pets.insert(1, \'chicken\') = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')

pets.remove('cat')

print('pets.remove(\'cat\') = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')

pets.reverse()

print('pets.reverse() = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')

pets.sort()

print('pets.sort() = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')

pets.sort(reverse=True)

print('pets.sort(reverse=True) = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')
