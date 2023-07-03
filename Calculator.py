from calc_art import logo
print(logo)
end='n'
while end=='n':
    n1=float(input("Enter a number: "))
    ask='y'
    while ask=='y':
        def add(n1,n2):
            return n1+n2
        def sub(n1,n2):
            return n1-n2
        def multi(n1,n2):
            return n1*n2
        def div(n1,n2):
            return n1/n2
        calc=input(" + \n - \n * \n / \n")
        n2=float(input("Enter next number: "))
        operations={'+':add(n1,n2),'-':sub(n1,n2),'*':multi(n1,n2),'/':div(n1,n2)}
        print(f"{n1}{calc}{n2} = {operations[calc]}")
        ask=input(f"Do you want to continue with the answer {operations[calc]}? y/n ").lower()
        if ask=='y':
            n1=operations[calc]
        else:
            end=input("Do you want to close the calculator? y/n ").lower()
    
