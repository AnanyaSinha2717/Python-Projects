print("Check leap year")
y=int(input("which year do you want to check? "))
if y%4==0 and y%100!=0:
    print("leap")
if y%4==0 and y%100==0:
    if y%400==0:
        print("leap")
    if y%400!=0:
        print("not a leap")
elif y%4!=0:
    print("not a leap year")
