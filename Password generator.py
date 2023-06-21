import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

s1=''
for x in range(1,nr_letters+1):
    a=random.choice(letters)
    s1+=a

s2=''
for y in range(1,nr_symbols+1):
    a=random.choice(symbols)
    s2+=a

s3=''
for z in range(1,nr_numbers+1):
    a=random.choice(numbers)
    s3+=a
print(f"your password in order is: {s1+s2+s3}")
#shuffling str without using list
'''
shuffled_pw=random.sample(s1+s2+s3,len(s1+s2+s3))
result=''.join(shuffled_pw)
'''
#shuffling str using list
l=list(s1+s2+s3)
random.shuffle(l)
result=''.join(l)

print(f"your shuffled password is: {result}")

c=input("press Enter to close")
