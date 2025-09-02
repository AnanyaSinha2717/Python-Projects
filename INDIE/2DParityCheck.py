d = []

a = 65
while a < 73:
    b = bin(a)[2:]
    b = b.zfill(8)
    d.append(list(b))
    a += 1

d.append([])
print(d)

# vrc
sum = 0
for i in range(0, 8, 1):
    for j in range(0, 8, 1):
        if d[i][j] == '1':
            sum += 1
    if sum % 2 == 0:
        d[i].append('0')
    else:
        d[i].append('1')
    sum = 0

#lrc
sum = 0
for i in range(0, 8, 1):
    for j in range(0, 8, 1):
        if d[j][i] == '1':
            sum += 1
    if sum % 2 == 0:
        d[8].append('0')
    else:
        d[8].append('1')
    sum = 0

print(d)