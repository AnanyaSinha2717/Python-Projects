def xor(a, b):
    if a == b:
        return '0'
    else:
        return '1'

d = "111010"   # message bits
p = "1010"     # generator polynomial

r = len(p) - 1
d = d + '0' * r   # append r zeros
d = list(d)
p = list(p)

for i in range(len(d) - r):
    if d[i] == '1':  # divide only if leading bit is 1
        for j in range(len(p)):
            d[i + j] = xor(d[i + j], p[j])

remainder = ''.join(d[-r:])
print("Remainder:", remainder)
