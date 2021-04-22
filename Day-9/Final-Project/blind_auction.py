import os
from art import logo

print(logo,end="\n")

bids = {}
bidding_finished = False

def highest_bidder (bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount  = bidding_record[bidder]
    if (bid_amount > highest_bid):
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")    



while not (bidding_finished):
  name = input ("What's your name? ")
  price = int(input ("What's your bid? $"))
  bids[name] = price
  should_continue = input ("Are there any bidders? Type 'yes' or 'no' \n")
  if (should_continue == 'no'):
    bidding_finished = True
    highest_bidder(bids)
  elif (should_continue == 'yes'):
    _ = os.system('cls')
    print(logo)






