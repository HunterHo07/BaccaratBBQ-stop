
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
for i in range(10):
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
    all_check_results.append(check_results)
    check_results=[]
    # print(i)
    
#clean up all results
print(all_check_results)


    

