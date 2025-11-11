#key=value format
contacts = dict(
    Jason = { 'phone': '555-0267', 'email': 'jason@'},
    Carl  = { 'phone': '555-0978', 'email': 'carl@'}
)

# 'key':value format
# contacts = { 
#       #key     value
#       'Jason': {'phone': '555-0267', 'email': 'jason@' },
#       'Carl' : {'phone': '555-0978', 'email': 'carl@' }   
# }

# + operator on strings, concat with space and newline!
for contact in contacts:
    print('key: ' + contact + '\t', contacts[contact]['email'], end=' \n')          
    # print('key: {} '.format(contact), end=' ')
    # print('\t email: ' + contacts[contact]['email'])               

