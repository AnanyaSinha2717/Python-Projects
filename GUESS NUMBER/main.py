import random
from guess_num_art import logo
print(logo)
print("WELCOME TO NUMBER GUESSING GAME")

def choice(n):
    for i in range(n):
        guess=int(input("Make a guess: "))
        if guess>num:
            print("Too High")
        elif guess<num:
            print("Too low")
        elif guess==num:
            print(f"$$ Yess! You got it! The answer was {num}. $$")
            break
        print(f"{(n-1)-i} move(s) left.")
    if guess!=num:
        print(f"!! Oops! You lost. The correct number was {num}. !!")

ask='y'
while ask=='y':        
    print("\n...I am thinking of a number between 1 to 100...")
    num=random.randint(1,100)
    lev=input("\nPick a mode - Type 'easy' or 'hard': ")
    if lev=='easy':
        print("You have 10 moves to guess the correct number.")
        choice(10)
    elif lev=='hard':
        print("You have 5 moves to guess the correct number.")
        choice(5)

    ask=input("\nDo you wanna play again? 'y'/'n': ").lower()
