r1=[11,21,31]
r2=[12,22,32]
r3=[13,23,33]
area=[r1,r2,r3]
print(f"{r1}\n{r2}\n{r3}")

pos=input("where do you want to put the treasure?")

horizontal=int(pos[0])
vertical=int(pos[1])
selected_row=area[vertical-1]
selected_row[horizontal-1]="X"

print(f"{r1}\n{r2}\n{r3}")
