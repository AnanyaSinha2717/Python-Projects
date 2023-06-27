def prime_checker(number):
    prime=True
    for x in range(2,number):
        if number%x==0:
            prime=False #not prime
    if prime and number!=1:
        print("It's a prime number.") 
    else:
        print("It's not a prime number.")

n=int(input("Enter the number you want to check: "))
prime_checker(number=n)

a=input("press Enter to continue.")
