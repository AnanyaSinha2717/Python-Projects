from replit import clear #doesn't work, use replit website to run the code
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("Welcome to the secret auction program")
d={}
more='y'
while more=='y':
    name=input("What is your name? ")
    bid=int(input("What's your bid? $"))
    d[name]=bid
    more=input("Are there any other bidders? y/n ").lower()
    clear()
l=[]
for i in d:
    l.append(d[i])
    m=max(l)
for x in d:
    if d[i]==m:
        print(f"The highest bid is by {i}, ${m}")
print(f"The names and bids of all bidders are\n{d}")
