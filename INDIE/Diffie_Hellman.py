def power(a, b, c):
    if b == 1:
        return a
    return pow(a, b)%c

#both users have p and q. one user has a, other b...
p = int(input("Public P: "))
q = int(input("Punlic Q: ")) #prime number
a = int(input("Private a: "))
#key generated
r1 = power(p, a, q)

b = int(input("Private b: "))
r2 = power(p, b, q)

#keys r1 and r2 are exchanged
#secret key is
k1 = power(r2, a, q)
k2 = power(r1, b, q)

if k1 == k2:
    print("key recieved = ", k1, " and ", k2)
else:
    print("error")

secret = "midwest indigo"

encryption = ''.join(chr(ord(ch) + k1) for ch in secret)
    
print("encrypted: ", encryption) 

decryption = ''.join(chr(ord(ch) - k1) for ch in encryption)
    
print("decrypted: ", decryption) 