print("Tip distribution")
b=float(input("what was the bill?  $"))
p=int(input("what percentage tip? 10,12 or 15? "))
people=int(input("how many people to split the bill? "))
tip=p/100 * b
total=(b+tip)/people
final=round(total, 2)
print(f"each person has to pay  ${final}")

a=input("press Enter to close")
