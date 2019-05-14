print(f'enter numbers: x y z n')
x = int(input())
y = int(input())
z = int(input())
n = int(input())

ar = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if ((i+j+k) != n):
#                 ar.append([i, j, k])

# use generators for a better version
ar = [(i, j, k) for i in range(x+1)
      for j in range(y+1)
      for k in range(z+1) if ((i+j+k) != n)]


print(ar)
print(len(ar))

# sample input
# 2
# 2
# 2
# 2
# sample output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]