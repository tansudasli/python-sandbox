contacts = {
    'Jason' : {
        'phone': '555-0267',
        'email': 'jason@'
    },
    'Carl' : {
        'phone': '555-0978',
        'email': 'carl@'
    }    
}

for contact in contacts:
    print('{} info'.format(contact))
    print('  ' + contacts[contact]['email'])
    
