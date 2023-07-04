enemies=1
def game():
    print("Enemies inside function: {enemies}")
    return enemies + 1
enemies=game()
print("Enemies outside fcn: {enemies}")


    
