from replit import clear
from art import logo

print(logo)
print("Welcome TO the Secret Acution Program")
bid = {}
bidding = False


def finding_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")


while not bidding:
    name = input("What is your Name? ")
    price = int(input("What's your Bid: $"))
    bid[name] = price
    ask = input("Are there any other to bid? type 'yes' or 'no'")
    if ask == "no":
        bidding = True
        finding_highest_bid(bid)
    elif ask == "yes":
        clear()
