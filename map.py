nameMap = {'Ali': [1, 250], 'Salih': [2, 120], 'Mahmut': 4}

aliCount = nameMap['Ali']


print('Map key:Values {}'.format(nameMap))
print('total len {}'.format(len(nameMap)))
print('count of Ali: {}'.format(aliCount))

del nameMap['Ali']
print('Map key:Values after deletion {}'.format(nameMap)) 

for name in nameMap:
    print('name {}'.format(name))

for values in nameMap['Salih']:
    print('values {}'.format(values))
    

if 'Mahmut' in nameMap.keys():
    print(nameMap['Mahmut'])

print('4' in nameMap.values())

# accessing both key and values
for k, v in nameMap.items():
    print('key is {}: {} value'.format(k, v))


nameMap.values

