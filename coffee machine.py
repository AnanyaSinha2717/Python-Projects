#initial

MENU = {"espresso": {"ingredients": {"water": 50, "coffee": 18,},"cost": 1.5,},
        
        "latte": {"ingredients": {"water": 200, "milk": 150,"coffee": 24,},"cost": 2.5,},
        
        "cappuccino": {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0,}
        }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("WELCOME TO THE CAFE")

#money
def money(ask):
    profit=0
    t=int(input("How many quarters?: "))*0.25
    t+=int(input("How many dimes?: "))*0.10
    t+=int(input("How many nickels?: "))*0.05
    t+=int(input("How many pennies?: "))*0.01
    print(f"You paid: ${round(t,2)}")
   
    if t>MENU[ask]['cost']:
        change=t-MENU[ask]['cost']
        print(f"Here is ${round(change,2)} in change.")
        profit+=MENU[ask]['cost']
        print(f"Here is your {ask} ☕. Enjoy!")
        
    elif t==MENU[ask]['cost']:
        profit+=MENU[ask]['cost'] 
        print(f"Here is your {ask} ☕. Enjoy!")
        
    elif t<MENU[ask]['cost']:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False
    return True
 
#order
def order(ask):
    for i in MENU[ask]['ingredients']:
        if resources[i]>=MENU[ask]['ingredients'][i]:
            resources[i]=resources[i]-MENU[ask]['ingredients'][i]
            print(f"{i}={resources[i]}")
        money(ask)
def suff()           
    if resources[i]<MENU[ask]['ingredients'][i]:
        print(f"Sorry, not enough {i}.")
        return False
    return True
        
            
on=True
while on:
    ask=input("What do you wanna order? ('latte', 'espresso', 'cappuccino')").lower()
    if ask=='report':
        print(f"water = {resources[water]}")
        print(f"milk = {resources[milk]}")
        print(f"coffee = {resources[coffee]}")
    elif ask=='off':
        on=False
    else:
        order(ask)



    
