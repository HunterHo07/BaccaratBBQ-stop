import random
from math import *

show1 = 0

#step 1
# Create Baccarat Deck & Shuffle & Discards
def create_shoe():
	cards_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0] 	# 13-cards created	['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 10, J, Q, K = 0 | A = 1
	deck = cards_set * 4 									          # 4 set of cards 13cards each
	table_deck = deck * 8 								          # 8 of decks for 1 table
	random.shuffle(table_deck)						          # shuffle Deck 1
	random.shuffle(table_deck)						          # shuffle Deck 2-time to be sure
	discard = table_deck[0]								          # discard process, draw 1st card of the deck
	if discard == 0: discard = 10							      # discard process, if 1st card is face or ten then discards 10
	table_deck_ready = table_deck[discard+1:]				# discard process, if 1st card is face or ten then discards 10 + 1, Else follow the number + 1

 # insert RED cards = cut cards to stop the deck from casino
	red = random.randint(290,320)			              # Get a random cut card position by random (208 = 50%) (300-320 = 25% left)
	# red = random.randint(27,30)			              # Get a random cut card position by random (208 = 50%) (260-290 = 30% left) Testing use
	table_deck_ready.insert(red,"STOP")             # Insert RED-CARD for Last round game of Baccarat cut-cards.
  

	check_deck = [discard, table_deck_ready ,table_deck]	#discards number, already discarded decks, original decks that has shuffle
	# print(*check_deck,sep='\n')							# To check the table deck ready
 
	# return len(table_deck)
	return table_deck_ready
# play_shoe()



#Step 2
# Play the game
Start_Play_Deck = create_shoe()							# Take the ready deck to action and start to play the game of baccarat
Table_Number = 0                            # Table Number as record
def play_game():										        # Game start play
  Game_results = []                         # record game results
  Win_row = 1                               # record same winning side count / Start with 1
  Win_results = ""                        # record which side winning, P, B, T
  Win_results_past = ""                   # record which side winning, P, B, T from the past 1 game compare with past and now
  Table_deck = Start_Play_Deck						# Mirror the ready deck for this table (So we can always check back the original deck)
  Red_Card = False
  Game_Count = 0                          # game counter

  #repeat the deck till RED-Card draw and stop
  while Red_Card == False:
      # print(Table_deck)									    # check original deck before play
      Game_Count+=1
      
      #draw hand from the decks
      for i in range(4):
        check_card = Table_deck.pop(0)
        if check_card == "STOP":                    #check if the red card is draw
          Red_Card = True
          # print("STOP")
          check_card = Table_deck.pop(0)
        if i == 0: player1 = check_card							#player draw 1st card
        if i == 1: banker1 = check_card							#banker draw 2nd card
        if i == 2: player2 = check_card							#player draw 1st card
        if i == 3: banker2 = check_card							#player draw 2nd card
      
      # print(player1 ,player2)								#check player face-up cards
      # print(banker1, banker2)								#check banker face-up cards
      
      #check player & banker hand total value
      player_hand = (player1 + player2) % 10				#Process player hands & -10 if the both cards add-up more than 10
      banker_hand = (banker1 + banker2) % 10				#Process banker hands & -10 if the both cards add-up more than 10
      player3 = ''
      banker3 = ''
      # print(Table_deck)									#check Decks after drew cards

# banker 9,8 = Done | 7
# Player 9,8 = Done
      if (player_hand < 8 and banker_hand < 8):			#if no natural win then check for 3rd card draw for player or banker
        #check player or banker need to draw 3rd card
          if player_hand <= 5:                           #player total 0,1,2,3,4 5, then player draw 3rd card
            check_card = Table_deck.pop(0)
            if check_card == "STOP":                          #check if the red card is draw
              Red_Card = True
              check_card = Table_deck.pop(0)
            player3 = check_card							                #player draw 3rd card
            player_hand = (player1 + player2 + player3) % 10	#Process player hands & -10 if the both cards add-up more than 10

            #check banker 3rd card draw condition
            if(banker_hand <= 2) or (banker_hand == 3 and player3 != 8) or (banker_hand == 4 and player3 >= 2 and player3 <= 7) or (banker_hand == 5 and player3 >= 4 and player3 <= 7) or (banker_hand == 6 and (player3 == 6 or player3 == 7)):
              check_card = Table_deck.pop(0)
              if check_card == "STOP":                        #check if the red card is draw
                Red_Card = True
                check_card = Table_deck.pop(0)
              banker3 = check_card							              #banker draw 3rd card
              banker_hand = (banker1 + banker2 + banker3) % 10#Process banker hands & -10 if the both cards add-up more than 10

          elif banker_hand <= 5 and (player_hand == 6 or player_hand == 7):
            check_card = Table_deck.pop(0)
            if check_card == "STOP":                        #check if the red card is draw
              Red_Card = True
              check_card = Table_deck.pop(0)
            banker3 = check_card							              #banker draw 3rd card
            banker_hand = (banker1 + banker2 + banker3) % 10#Process banker hands & -10 if the both cards add-up more than 10

      
      # print('Player_Hand:', player1, player2, player3,'=', player_hand)					#check player face-up cards ***********************
      # print('Banker_Hand:', banker1, banker2, banker3,'=', banker_hand)					#check banker face-up cards ***********************
      # print(Table_deck)									#check Decks after drew cards

      
      #check player or banker win or Tie
      if (player_hand > banker_hand):
        Win_results = "P"
        # print("P-WIN")
      elif (player_hand < banker_hand):
        Win_results = "B"
        # print("BB-WIN")
      else:
        Win_results = "T"
        # print("TIE")

      #check if winning in row
      if Win_results_past == Win_results: 
        Win_row += 1
      elif Win_results_past == '':
        pass
      else:
        Game_results = Game_results + [Win_results+str(Win_row)]
        Win_row = 1
      if Red_Card == True:
        Game_results = Game_results + [Win_results+str(Win_row)]


      # print(Win_results_past ,Win_results)            # Check each winning row
      Win_results_past = Win_results
      # print(Game_Count, Game_results)
  print(Game_Count, Game_results)
      
play_game()
