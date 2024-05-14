import random
from hangman_words import word_list
from hangman_art import Stages, logo, clear

print(logo)
chosen_word=(random.choice(word_list)).upper()
len_cword=len(chosen_word)
lives=6
temp=0
print(chosen_word)

display=[]
for i in range(len_cword):
    display.append("_")
print(f"{' '.join(display)}")

while '_' in display:
    guess=input("Guess a letter:").upper()
    clear()
    print(logo)
    if guess in display:
        print(f"You've already guessed {guess}")
        
    else: 
        if guess not in chosen_word:
            print(f"Your guess {guess}, is not in the word")
            lives-=1
            if lives<0:
                print("You lose.")
                break
        else: 
            for pos in range(len_cword):
                if guess==chosen_word[pos]:
                    display[pos]=guess               
    print(f"{' '.join(display)}")
    print(Stages[lives])
    
else:
    print("You have won.")
