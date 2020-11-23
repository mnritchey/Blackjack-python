from art import logo
import random
from os import system, name

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def clear():
  if name == "nt":
    _ = system("cls")
  else: 
    _ = system("clear")

def deal_card():
  """Returns random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  return sum(cards)

def compare(user_score, comp_score):
  """Check the scores to see who will win"""
  if user_score == comp_score:
    return "Draw"
  elif comp_score == 0: 
    return "Lose, opponent has Blackjack"
  elif user_score == 0: 
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose."
  elif comp_score > 21: 
    return "Opponent went over. You win."
  elif user_score > comp_score:
    return "You win"
  else:
    return "You lose"

def play_game():

  print(logo)

  user_cards = []
  comp_cards = []
  is_game_over = False

        # deal two cards to start the game
  for _ in range(2): 
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)

    print(f"    Your cards: {user_cards}. Current score: {user_score}.")
    print(f"    Computer's first card is {comp_cards[0]}.")

    if user_score == 0 or comp_score == 0 or user_score > 21:
      is_game_over = True
    else: 
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else: 
        is_game_over = True
  while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)


  print(f"    Your cards: {user_cards}. Current score: {user_score}")
  print(f"    Computer's cards: {comp_cards}. Computer score: {comp_score}")
  print(compare(user_score, comp_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
  
