def star(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print("1 ", end='')
            else:
                print("0 ", end='')
        print()

def mesh(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print("0 ", end='')
            else:
                print("1 ", end='')
        print()

n = int(input("number of nodes: "))
print("star topology:\n")
star(n)

print("mesh topology:\n")
mesh(n)