print("Hello! We will be playing PYJACK today.")
print('\n')

print("The rules are as follows: ")
print("  'Hit' means you want another card.")
print("  'Stand' means you want no more cards.")
print("  If your total total exceeds 21, you lose.")
print("  If the Dealer's total exceeds 21, you win.")
print("  Note that if you have an exact total score of 21, you win automatically!")
print('\n')
print("Let's begin. May the best player win!")
print('\n')

import random 
deck = [2,3,4,5,6,7,8,9,10]*4
random.shuffle(deck)

player_deck = []
dealer_deck = []

def deal_deck():
 return deck.pop()

player_deck.append(deal_deck())
print(f"Your cards are {player_deck}\n")

dealer_deck.append(deal_deck())
print(f"The dealer's cards are {dealer_deck}\n")

while True:
  n = input("Would you like to hit or stand? ").lower()
  if n == "hit":
     player_deck.append(deal_deck())
     print(f"Your cards are {player_deck}\n")
  elif n == "stand": 
     print("\n")
     break
  else:
     print("Invalid Input. Enter either 'hit' or 'stand'\n")

sum_player = 0
sum_dealer = 0

for i in player_deck:
  sum_player = sum_player + i
print(f"{sum_player} is the your total score.\n")

if sum_player == 21:
  print("You win with a perfect score!")
elif sum_player > 21:
  print("Dealer wins! You went over 21.")
else:
  print(f"The dealer's first card was {dealer_deck}")
  while sum_dealer < 17:
    dealer_deck.append(deal_deck())
    print(f"The dealer's cards are {dealer_deck}")

    sum_dealer = 0
    for j in dealer_deck:
      sum_dealer = sum_dealer + j

  print(f"\n{sum_dealer} is the dealer's total score.\n")

if sum_dealer == 21:
  print("Dealer wins with a perfect score!")
elif sum_player == 21 or sum_player > 21:
  print('\n')
elif sum_dealer == sum_player:
  print("It is a tie!")
elif sum_dealer > 21: 
  print("You win! Dealer went over 21.")
elif sum_player < 21 and sum_dealer < 21 and sum_player > sum_dealer:
  print("You win!")
elif sum_player < 21 and sum_dealer < 21 and sum_player < sum_dealer:
 print("Dealer wins!")
else:
  print('\n')