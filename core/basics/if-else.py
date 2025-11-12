#run-command
# echo 120 | python3 if-else.py

age = int(input())

msg = 'greater than 40' if age >= 40 else ('greater than 30 but less than 40' if age >=30 else 'less than 30')

print(msg)

# if age >= 40:
#     print('greater than 40')
# elif age >= 30:
#     print("greater than 30 but less than 40")
# else:
#     print('less than 30')
