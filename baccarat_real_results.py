
# results from : https://wizardofodds.com/games/baccarat/basics/#simulations
# // read results from txt bac1 - bac10
# with open("real_results/bac1.txt") as file:
#     lines = file.readlines()
#     lines = [line.rstrip() for line in lines]

with open('real_results/bac1.txt') as f:
    lines = f.read().splitlines()
# print(lines[0])

results_holder = []
#get the 25,000 results & clean it
for i in range(25000):
    results_holder = results_holder + [lines[i]]

# remove all Tie from the results
results_holder = [s.replace(',T', '') for s in results_holder] # 
results_holder = [s.replace('T', '') for s in results_holder] # 
results_holder = [s.replace('0', '') for s in results_holder] #
results_holder = [s.replace('1', '') for s in results_holder] #
results_holder = [s.replace('2', '') for s in results_holder] #
results_holder = [s.replace('3', '') for s in results_holder] #
results_holder = [s.replace('4', '') for s in results_holder] #
results_holder = [s.replace('5', '') for s in results_holder] #
results_holder = [s.replace('6', '') for s in results_holder] #
results_holder = [s.replace('7', '') for s in results_holder] #
results_holder = [s.replace('8', '') for s in results_holder] #
results_holder = [s.replace('9', '') for s in results_holder] #
# remove all , from the results
results_holder = [s.replace(',', '') for s in results_holder] # 

# print(results_holder)

check_results = []
all_check_results = []
# print(check_results)
now           = 'NO'
past          = ''
win_count     = 1
game_count    = 1
for i in results_holder:
    for u in i:
        now = u
        # print(u)
        if now == past:
            win_count+=1
        elif past == '':
            pass
        else:
            check_results = check_results + [past+str(win_count)]
            win_count=1
        past = now
    if check_results[0][0] == "P":
        # print(check_results, "Before")
        check_results = check_results[1:]
        # print(check_results, "After")
    all_check_results.append(check_results)
    check_results=[]
    # print(i)

#clean up all results
# print(all_check_results)









# Step 5 play many tables simulation
def test_7():
  W1_win   = 0
  L1_lose  = 0
  W2_win   = 0
  L2_lose  = 0
  W3_win   = 0
  L3_lose  = 0
  skip     = 0 
  skip1    = 0 
  skip_win = 0 
  skip1_win= 0
  for test_1 in all_check_results:  #10k results about 4.5sec
    # test_1 = test_case()       # Take the results from random game
    # print(test_1)

    # Bet all & Check
    #Bet-1
    if int(test_1[0][1]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
      L1_lose+=1
    else:
      W1_win+=1

      #Bet-2
      if int(test_1[2][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
        L1_lose+=3
      else:
        W1_win+=1

        #Bet-3
        if int(test_1[4][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
          L1_lose+=3
        else:
          W1_win+=1


    #Bet-1
    if skip > 2:
      #Bet-1
      if int(test_1[0][1]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        L2_lose+=1
        skip=0
      else:
        W2_win+=1
        skip_win+=1

        #Bet-2
        if int(test_1[2][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
          L2_lose+=1
          skip=0
        else:
          W2_win+=1
          skip_win+=1

          #Bet-3
          if int(test_1[4][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
            L2_lose+=3
            skip=0
          else:
            W2_win+=1
            skip_win+=1

    if int(test_1[0][1]) > 2 and int(test_1[2][1]) > 2:
      skip+=1
    if skip_win > 8:
      skip_win=0
      skip=0


    #Bet-1
    if skip1 > 2:
      #Bet-1
      if int(test_1[0][1]) > 1:  #if 1st or 2nd B- is more than 3 win in the row
        L3_lose+=1
        skip1=0
      else:
        W3_win+=1
        skip1_win+=1

        #Bet-2
        if int(test_1[2][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
          L3_lose+=1
          skip1=0
        else:
          W3_win+=1
          skip1_win+=1

          #Bet-3
          if int(test_1[4][1]) > 2:  #if 1st or 2nd B- is more than 3 win in the row
            L3_lose+=3
            skip1=0
          else:
            W3_win+=1
            skip1_win+=1

    if int(test_1[0][1]) > 2 and int(test_1[2][1]) > 2:
      skip1+=1
    if skip1_win > 7:
      skip1_win=0
      skip1=0



    # print(i,  "=" ,test_1)
    # print("Win-1:", round(W_win,2) , " | Win-2:", round(L_lose,2) , " || Total:", round(total,2))
  total3 = W3_win - L3_lose
  total_3 = W3_win + L3_lose
  total_per3 = (W3_win / total_3) * 100 #2.3 - 5.51
  total2 = W2_win - L2_lose
  total_2 = W2_win + L2_lose
  total_per2 = (W2_win / total_2) * 100 #2.3 - 5.51
  total1 = W1_win - L1_lose
  total_1 = W1_win + L1_lose
  total_per1 = (W1_win / total_1) * 100 #2.3 - 5.51
  print("1-0 Win-1:", round(W1_win,2) , " | Lose-1:", round(L1_lose,2) , " || Total-1:", round(total1,2) , "|", round(total_per1,2))
  print("1-1 Win-2:", round(W2_win,2) , " | Lose-2:", round(L2_lose,2) , " || Total-2:", round(total2,2) , "|", round(total_per2,2))
  print("1-2 Win-3:", round(W3_win,2) , " | Lose-3:", round(L3_lose,2) , " || Total-3:", round(total3,2) , "|", round(total_per3,2))

# 1-0 Win-1: 21651  | Lose-1: 28161  || Total-1: -6510 | 43.47
# 1-1 Win-2: 763  | Lose-2: 884  || Total-2: -121 | 46.33
# 1-2 Win-3: 761  | Lose-3: 874  || Total-3: -113 | 46.54
test_7()
    

