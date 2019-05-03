contacts = dict(
    Jason={
        'phone': '555-0267',
        'email': 'jason@'},
    Carl={
        'phone': '555-0978',
        'email': 'carl@'}
)

#
# contacts = {
#     'Jason': {
#         'phone': '555-0267',
#         'email': 'jason@'
#     },
#     'Carl': {
#         'phone': '555-0978',
#         'email': 'carl@'
#     }
# }
#

for contact in contacts:
    print('keys are: {} '.format(contact))
    print('\t email: ' + contacts[contact]['email'])

