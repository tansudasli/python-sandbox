
animalList = ['bear', 'cat', 'tiger', 'donkey']

print(animalList[0])


# dynamic. no separate for array or arraylist
animalList.extend(['duck'])
animalList = animalList + ['mammut', 'cow']

# animalList.append


print('animals {}'.format(animalList))

animalList.insert(2, 'duck')

# no toString method.
print(animalList)

print(30 * "-")

# operator overloading
print('fist two of animals {}'.format(animalList[0:2]))
print('last two of animals {}'.format(animalList[-2:]))


def find(animal):
    try:
        return animalList.index(animal)
    except IndexError:
        return -1


print('duck index {}'.format(find('duck')))

print('-' * 30)

counter = 0
for animal in animalList:
    counter = counter + 1
    print(str(counter) + '/' + str(len(animalList)) + ': ' + animal.upper())

print('-' * 30)

animalList.sort()
print('sorted animals {}'.format(animalList))

# some samples of
# range(2, 4)
# range(1, 10, 2)
for item in range(3):
    print(animalList[item])

# normally we should write additional steps in java
print('-' * 30)
for item in range(0, len(animalList), 2):
    print(animalList[item])



