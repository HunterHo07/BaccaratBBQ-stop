import random
from math import *

show1 = 0

# Create Baccarat Deck & Shuffle & Discards
def play_shoe():
	cards_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] 	# 13-cards created
	deck = cards_set * 4 									# 4 set of cards 13cards each
	table_deck = deck * 8 									# 8 of decks for 1 table
	random.shuffle(table_deck)								# shuffle Deck 1
	random.shuffle(table_deck)								# shuffle Deck 2-time to be sure
	discard = table_deck[0]									# discard process, draw 1st card of the deck
	if discard == 0: discard = 10							# discard process, if 1st card is face or ten then discards 10
 
	table_deck_ready = table_deck[discard+1:]				# discard process, if 1st card is face or ten then discards 10 + 1, Else follow the number + 1

	# return len(table_deck)
	return table_deck_ready

print(play_shoe())






