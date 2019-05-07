# echo 120 | python3 if-else.py

age = int(input())

if age >= 40:
    print('greater than 40')
elif age >= 30:
    print("greater than 30 but less than 40")
else:
    print('less than 30')
