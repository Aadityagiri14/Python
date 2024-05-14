from art import clear, logo
import random

card=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def display(users, comp,flag):
    print(f"Your cards: {users}, current score={sum(users)}")
    if flag==1:
            print(f"Computer's first card: {comp[0]}")
    elif flag<len(comp):
            print(f"Computer's card: {comp[0]}, {comp[1]}")
    else:
        print(f"Computer's final hand: {comp}, score={sum(comp)}")
    
    
def cards():
    random.choice(card)
    
    
def check(users,comp):
    U=sum(users)
    C=sum(comp)
    if U==21 or ((U > C or C>21) and U<=21):
        if U==C:
            print("It's a Draw.")
            return
        print("You won.")
    elif U>21:
        print("You went over. You loose.")
    elif U==C:
        print("It's a Draw.")
    else:
        print("You loose.")
    
def ace_check(player):
    if 11 in player and sum(player)>21:
        player[player.index(11)]=int(input("You got an ace. What vale should it have '11' or '1'? "))
        display(Players_cards,Computers_cards,flag)
        
        
def bj():
    
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=="y":
        clear()
        print(logo)
        flag=1
        Players_cards=[]
        Computers_cards=[]
        
        for i in range(2):
            Players_cards.append(cards())
            Computers_cards.append(cards())
        display(Players_cards,Computers_cards,flag)
        ace_check(Players_cards)
        
        while sum(Computers_cards)<17:
            Computers_cards.append(cards())
            flag+=1
            print("Computer got another card.")
            display(Players_cards,Computers_cards,flag)
        
        if input("Type 'y' to get another card, type 'n' to pass:") == "y":
            Players_cards.append(cards())
            display(Players_cards,Computers_cards,flag)
        flag+=1
        display(Players_cards,Computers_cards,flag)
        check(Players_cards,Computers_cards)
                
            
bj()