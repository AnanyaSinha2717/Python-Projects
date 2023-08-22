enemies=1
def game():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1
enemies=game()
print(f"Enemies outside fcn: {enemies}")

a=input("press ENTER to close")
