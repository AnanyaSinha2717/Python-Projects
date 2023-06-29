import random
end=False
while end==False:
    q=input("Choose rock(1),paper(2) or scissors(3): ")
    rock='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    paper='''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    scissors='''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    if q==1:
        print(f"You chose: rock {rock}")
    elif q==2:
        print(f"You chose: paper {paper}")
    else:
        print(f"You chose: scissors {scissors}")

    x=random.randint(0,2)
    if x==0:
        print(f"Computer chose: rock {rock}")
    elif x==1:
        print(f"Computer chose: paper {paper}")
    elif x==2:
        print(f"Computer chose: scissors {scissors}")

    if q==1:
        if x==0:
            print("Tie\n")
        elif x==1:
            print("You lost\n")
        elif x==2:
            print("You won\n")
    elif q==2:
        if x==0:
            print("You won\n")
        elif x==1:
            print("Tie\n")
        elif x==2:
            print("You lost\n")
    else:
        if x==0:
            print("You lost\n")
        elif x==1:
            print("You won\n")
        elif x==2:
            print("Tie\n")

    ask=input("Do you want to continue? y/n: ").lower()
    if ask=='y':
        end=False
    else:
        end=True


