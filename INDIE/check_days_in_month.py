print("Check days in month")
ask='y'
while ask=='y':
    leap=True
    year=int(input("Enter a year: "))
    month=int(input("Enter the month's number: "))
    if year%4==0 and year%100!=0:
        leap=True
    if year%4==0 and year%100==0:
        if year%400==0:
            leap=True
        if year%400!=0:
            leap=False
    elif year%4!=0:
        leap=False

    def days_in_month(year,month):
        month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
        if leap==True:
            if month==2:
                print('29')
        else:
            print(month_days[month-1])
        
    days=days_in_month(year,month)
            
    ask=input("Do you want to continue? y/n ").lower()

