import random

from hangman_art import logo

end=False
lives=6

from hangman_words import word_list
chosen_word=list(word_list[random.randint(0,len(word_list))])

display=[]
for i in chosen_word:
    display+='_'
print(display)

guessed_before=[]

while not end:
    guess=input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have guessed '{guess}' before")
        
    for g in range(len(chosen_word)):
        x=chosen_word[g]
        if x==guess:
            display[g]=x
            
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word, you lose a life")
        lives-=1
        if lives==0:
            end=True
            print("You lost")
            print(f"The correct word was '{''.join(chosen_word)}'")

    print(' '.join(display))
    
    if '_' not in display:
        end=True
        print("You won.")
        print(f"The correct word is '{''.join(chosen_word)}'")
        
    from hangman_art import stages
    print(stages[lives])

a=input("press Enter to leave")
