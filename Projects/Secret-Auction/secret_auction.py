from secret_art import logo, clear

print(logo)

bids={}
other_bidder="yes"

def highest_bidder(bids):
    highest_bid=0
    for key in bids:
        if bids[key]>highest_bid:
            highest_bid=bids[key]
            highest_bidder=key
    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
            
            
while other_bidder=="yes":
    name=input("What is your name?:")
    bid=int(input("What's your bid?: $"))
    bids[name]=bid
    other_bidder=input("Are there any other bidders? Type 'yes' or 'no'.")
    clear()
    if other_bidder=="no":
        highest_bidder(bids)
        
