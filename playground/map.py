nameMap = {'Ali': [1, 250], 'Salih': [2, 120], 'Mahmut': 4}
print(type(nameMap))

valueOfALI = nameMap['Ali']


# print(nameMap)

print('Map key:Values {}'.format(nameMap))
print('total len {}'.format(len(nameMap)))
print('count of Ali: {}'.format(valueOfALI))

# del nameMap['Ali']
# print('Map key:Values after deletion {}'.format(nameMap))

print(30 * "-")
for name in nameMap:
    print('name {}'.format(name))

print(30 * "-")
for values in nameMap['Salih']:
    print('values of Salih {}'.format(values))

print(30 * "-")

if 'Mahmut' in nameMap.keys():
    print("Mahmut is valid key")
    print(nameMap['Mahmut'])

print(4 in nameMap.values())

print(30 * "-")

# accessing both key and values
for k, v in nameMap.items():
    print('key is {}: {} value'.format(k, v))



