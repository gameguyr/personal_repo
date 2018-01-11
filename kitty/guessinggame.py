import random
from collections import Counter
import matplotlib
import pylab
user_win_count = 0
comp_win_count = 0
tie_count = 0
check_move = 2
past_move = 0
average = 10
total_games = 1000
user_win = [0 for i in range(check_move+50)]
user_range = [0 for i in range(check_move+50)]
user_total = [0 for i in range(check_move+50)]
for k in range(1,average):
    check_move = 2
    past_move = 0
    for i in range(check_move,check_move+50):
        user_choices = [0 for j in range(i)]
        user_win_count = 0
        comp_win_count = 0
        tie_count = 0
        while(user_win_count < total_games):
        ##    user_pick = raw_input("Pick 1 or 2 or 3 :")
            user_pick = random.randint(1,3)
            user_choices[past_move] = int(user_pick)
            data = Counter(user_choices)
            if(past_move == i - 1):
                past_move = 0
            else:
                past_move = past_move + 1
            most_moved = data.most_common(1)
            if(most_moved[0][0] == 0):
                comp_pick = random.randint(1,3)
            if(most_moved[0][0] == 1):
                comp_pick = random.randint(1,2)
            if(most_moved[0][0] == 2):
                comp_pick = random.randint(2,3)
            if(most_moved[0][0] == 3):
                if(random.random() <= 0.5):
                    comp_pick = 1
                else:
                    comp_pick = 3
            
            if(int(user_pick) == int(comp_pick)):
                tie_count = tie_count + 1
            else:
                if(int(user_pick) == 1):
                    if(int(comp_pick) == 3):
                        user_win_count = user_win_count + 1
                    else:
                        comp_win_count = comp_win_count + 1
                if(int(user_pick) == 2):
                    if(int(comp_pick) == 1):
                        user_win_count = user_win_count + 1
                    else:
                        comp_win_count = comp_win_count + 1
                if(int(user_pick) == 3):
                    if(int(comp_pick) == 2):
                        user_win_count = user_win_count + 1
                    else:
                        comp_win_count = comp_win_count + 1
            
        win_prec = float(comp_win_count) /float((user_win_count + comp_win_count + tie_count))  
        user_win[i] = win_prec
        user_range[i] = i
	matplotlib.pyplot.scatter(user_range,user_win)
	matplotlib.pyplot.title("Number of Remember Moves Verse Win Percentage")
	matplotlib.pyplot.xlabel("Number Of Remembered Moves")
	matplotlib.pyplot.ylabel("Computer Won / Total Games")
	matplotlib.pyplot.xlim([check_move-1,check_move+11])
	matplotlib.pyplot.ylim([0.3,0.5])
    for m in range(len(user_win)):
        user_total[m] = user_total[m] + user_win[m]
for l in range(len(user_total)):
    user_total[l] = user_total[l]/(average-1)
print "Done!"

matplotlib.pyplot.scatter(user_range,user_total,color='red',label='Averaged Data')
matplotlib.pyplot.title("Number of Remember Moves Verse Win Percentage")
matplotlib.pyplot.xlabel("Number Of Remembered Moves")
matplotlib.pyplot.ylabel("Computer Won / Total Games")
matplotlib.pyplot.xlim([check_move-1,check_move+51])
matplotlib.pyplot.ylim([0.3,0.5])
l2 = matplotlib.pyplot.legend(loc='upper left')
l1 = matplotlib.pyplot.legend(['Individual Data'],loc='upper right')
matplotlib.pyplot.gca().add_artist(l1)
matplotlib.pyplot.gca().add_artist(l2)

matplotlib.pyplot.show()
