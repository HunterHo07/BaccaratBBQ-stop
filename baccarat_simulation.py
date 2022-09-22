import random
from math import *

show1 = 0

#step 1
# Create Baccarat Deck & Shuffle & Discards
def create_shoe():
	cards_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] 	# 13-cards created	['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 10, J, Q, K = 0 | A = 1
	deck = cards_set * 4 									# 4 set of cards 13cards each
	table_deck = deck * 8 									# 8 of decks for 1 table
	random.shuffle(table_deck)								# shuffle Deck 1
	random.shuffle(table_deck)								# shuffle Deck 2-time to be sure
	discard = table_deck[0]									# discard process, draw 1st card of the deck
	if discard == 0: discard = 10							# discard process, if 1st card is face or ten then discards 10
	table_deck_ready = table_deck[discard+1:]				# discard process, if 1st card is face or ten then discards 10 + 1, Else follow the number + 1
 
 # insert RED cards = cut cards to stop the deck from casino

	check_deck = [discard, table_deck_ready ,table_deck]	#discards number, already discarded decks, original decks that has shuffle
	# print(*check_deck,sep='\n')							# To check the table deck ready
 
	# return len(table_deck)
	return table_deck_ready
# play_shoe()



#Step 2
# Play the game
Start_Play_Deck = create_shoe()							# Take the ready deck to action and start to play the game of baccarat
def play_game():										# Game start play
    Table_deck = Start_Play_Deck						# Mirror the ready deck for this table (So we can always check back the original deck)
    print(Table_deck)									#check original deck before play
    
    player1 = Table_deck.pop(0)							#player draw 1st card
    banker1 = Table_deck.pop(0)							#banker draw 1st card
    player2 = Table_deck.pop(0)							#player draw 2nd card
    banker2 = Table_deck.pop(0)							#banker draw 1st card
    
    print(player1 ,player2)								#check player face-up cards
    print(banker1, banker2)								#check banker face-up cards
    print(Table_deck)									#check Decks after drew cards
    

play_game()