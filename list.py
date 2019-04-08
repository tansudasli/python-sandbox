
animaList = ['bear', 'cat', 'tiger', 'donkey']

# print(animaList[0])

# dynamic. no seperate for array or arraylist
animaList.extend(['duck'])
animaList = animaList + ['mammut', 'cow']
#animaList.append

print('animals {}'.format(animaList))
print('-' * 30)

animaList.insert(2, 'duck')

# no toString method.
print(animaList)

# operator overloading
print('fist two of animals {}'.format(animaList[0:2]))
print('last two of animals {}'.format(animaList[-2:]))

def find(animal):
    try:
        return animaList.index(animal)
    except:
        return -1
    
print('duck index {}'.format(find('duck')))

print('-' * 30)
counter = 0
for item in animaList:
    counter = counter + 1
    print(str(counter) + '/' + str(len(animaList)) + ': ' + item.upper())
print('-' * 30)

animaList.sort()
print('sorted animals {}'.format(animaList))

# some samples of
# range(2, 4)
# range(1, 10, 2)  
for item in range(3):
    print(animaList[item])

# normally we should write additional steps in java
print('-' * 30)
for item in range(0, len(animaList), 2):
    print(animaList[item])    


   
