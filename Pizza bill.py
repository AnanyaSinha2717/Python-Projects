print("Welcome to pizza place")
s=input("what size pizza?")
p=input("do you want pepperoni")
c=input("do you wany extra cheese")
bill=0
if s=="s":
    bill=15
    if p=='yes' and c=='no':
        bill+=2
        print(f"your bill is {bill}")
    elif p=='yes' and c=='yes':
        bill+=3
        print(f"bill is {bill}")
    elif p=='no' and c=='yes':
        bill+=1
        print(f"your bill is {bill}")
    else:
        print(f"your bill {bill}")

elif s=='m':
    bill=20
    if p=='yes' and c=='no':
        bill+=3
        print(f"your bill is {bill}")
    elif p=='yes' and c=='yes':
        bill+=4
        print(f"bill is {bill}")
    elif p=='no' and c=='yes':
        bill+=1
        print(f"your bill is {bill}")
    else:
        print(f"your bill {bill}")

elif s=='l':
    bill=25
    if p=='yes':
        if c=='no':
            bill+=3
            print(f"your bill is {bill}")
        elif c=='yes':
            bill+=4
            print(f"bill is {bill}")
    elif p=='no' and c=='yes':
        bill+=1
        print(f"your bill is {bill}")
    else:
        print(f"your bill {bill}")
