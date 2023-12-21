# n = [1,2,3]
# print("n =", n)
# new_n = [i+1 for i in n]
# print("new_n =", new_n)

name = "Lily"
new_n = [letter for letter in name]
print(new_n)

num_list = [i*2 for i in range(1,5)]
print(num_list)

names = ["lily", 'freddie', 'daya', 'salunkhe']
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)