# Random Choice and Shuffle
import random
pets = ['dog', 'cat', 'moose']

print('pets = [', end='')
for i, item in enumerate(pets):
    print(item, end='')
    if i == len(pets) - 1:
        print(']')
    else:
        print(', ', end='')

print("A random choice from the list: ", end='')
print(random.choice(pets))

print("Randomly shuffle the list: ", end='')
random.shuffle(pets)
print(pets)
