print("Welcome to love calculator")
n1=input("name of first person \n")
n2=input("name of second person \n")
l_n1=n1.lower()
l_n2=n2.lower()

t=l_n1.count("t")+l_n2.count("t")
r=l_n1.count("r")+l_n2.count("r")
u=l_n1.count("u")+l_n2.count("u")
e1=l_n1.count("e")+l_n2.count("e")

true=t+r+u+e1

l=l_n1.count("l")+l_n2.count("l")
o=l_n1.count("o")+l_n2.count("o")
v=l_n1.count("v")+l_n2.count("v")
e2=l_n1.count("e")+l_n2.count("e")

love=l+o+v+e2
ls=10*true + love
if ls<10 or ls>90:
    print(f"Your score is {ls}%, you need to get over it.")
elif ls>=40 and ls<=50:
    print(f"Your score is {ls}%, you go alright together.")
else:
    print(f"Your score is {ls}% ...pffft")

a=input("press Enter to close")
