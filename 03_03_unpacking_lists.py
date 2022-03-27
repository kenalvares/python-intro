# Unpacking lists
dog = ['black', 4, True, 'Iris']
color, numOfLegs, isHungry, name = dog

print('dog list: [', end='')
for i in range(len(dog)):
    print(dog[i], end=',')
print(']', end='\n\n')

print('Color of Dog: ' + color)
print('Number of Legs: ' + str(numOfLegs))
print('Is Dog Hungry: ' + str(isHungry))
print('Name of Dog: ' + name)
