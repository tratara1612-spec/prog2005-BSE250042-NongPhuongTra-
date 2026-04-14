# 2.1
n = int(input('Nhập số n: '))
for i in range(n):
    print(' * ' * n)

# 2.2
n = int(input('Nhập số n: '))
for i in range(n + 1):
    if 0 < i <= n:
        print(' * ' * i)
    else:
        continue

# 2.3
n = int(input('Nhập số n: '))
for i in range(n, 0, -1):
    if 0 < i <= n:
        print(' * ' * i)
    else:
        continue

# 2.4
n = int(input('Nhập n: '))
for i in range(n):
    for j in range(n):
        if j >= n - 1 - i:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

# 2.5
n = int(input('Nhập n: '))
for i in range(n):
    for j in range(n):
        if j == 0 or i == n - 1 or i == j:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

# 2.6
n = int(input('Nhập n: '))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j + i == n - 1:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

# 2.7
n = int(input('Nhập n: '))
for i in range(n):
    for j in range(n):
        if j == n - 1 or i == n - 1 or i + j == n - 1:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

# 2.8
n = int(input('Nhập n: '))
t = n * n
for i in range(n):
    p = ' * ' * (i + 1)
    print(p.center(t))

# 2.9
n = int(input('Nhập n: '))

for i in range(1, n + 1):
    if i == 1:
        p = '*'
    elif i == n:
        p = '* ' * n
    else:
        p = '*' + ' ' * (2 * i - 3) + '*'
    print(p.center(n * 2))

# 2.10
n = int(input('Nhập n: '))

for i in range(n, 0, -1):
    if i == 1:
        p = '*'
    elif i == n:
        p = '* ' * n
    else:
        p = '*' + ' ' * (2 * i - 3) + '*'
    print(p.center(2 * n))
