#3.1
n = int(input('Nhập số n: '))
for i in range(n):
    print(' 1 ' * n)
#3.2
n = int(input('Nhập số n: '))
for i in range(n):
    for j in range(1, n+1):
        print(j, end=' ')
    print()
#3.3
n = int(input('Nhập số n: '))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
#3.4
n = int(input('Nhập số n: '))
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
#3.5
n = int(input("Nhập n: "))
for i in range(1, n+1):
    if i ==1:
        print(1)
    elif i==n:
        print(*(range(1, n+1)))
    else:
        print(1, i, sep=' '*(2*i-3))
#3.6
n = int(input("Nhập n: "))
for i in range(n, 0, -1):
    if i ==1:
        print(1)
    elif i==n:
        print(*(range(1, n+1)))
    else:
        print(1, i, sep=' '*(2*i-3))
#3.7
n = int(input("Nhập n: "))
for i in range(1, n+1):
    print(' ' * (n-i), *([i]*i))

#3.8
n = int(input("Nhập n: "))
for i in range(1, n+1):
    r = list(range(1, i+1))+list(range(i-1,0, -1 ))
    print(' ' *(n-i), *r)
#3.9
n = int(input("Nhập n: "))
for i in range(1, n+1):
    if i ==1:
        p = '1'
    elif i==n:
        r = list(range(1, i+1))+list(range(i-1,0, -1 ))
        p= ' '.join(map(str,r))
    else:
        p = '1 ' + '  '*(2*i-3) + ' 1'
    print(p.center(4*n))
