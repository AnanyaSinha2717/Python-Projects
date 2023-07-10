from prettytable import PrettyTable
x=PrettyTable()
x.field_names=['Menu','Rate','Milk','Water','Coffee']
x.add_rows(
  [
    ['Espresso','$5','100ml','50ml','150g'],
    ['Latte','$3','150ml','0ml','100g']
  ]
)
x.align='c'
print(x)
