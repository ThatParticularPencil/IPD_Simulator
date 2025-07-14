
#Functions


import numpy as np
import random
import time
from IPDStrategies import Player_list, Player_dict,Tit_For_Tat

highest_avgs = [
    "Adaptive_Pavlov"
   ,"Five_Ninetyfive"
   ,"Defector"
   ,"Prober"
   ,"ProgressiveTFT"
   ,"Safe_Palov"
   ,"OmegaTFT"
   ,"TFtwoT"
   ,"Quick_Pavlov"
   ,"twoTFT"
   ,"Equalizer"
   ,"Grudger"
   ,"Tit_For_Tat"
   ,"ZeroDeterminant"
   ,"Behavioral_Pavlov"
   ,"Evil"
   ,"Gradual"
   ,"Forty_Sixty"
   ,"allC_then_Inverse"
   ,"ImperfectTFT"
   ,"susTFT"
   ,"Sore_loser"
   ,"Random_then_Inverse"
   ,"Random_Player"
   ,"Cooperator"
   ,"Probability"
   ,"Sixty_Forty"
   ,"Almost_Tit"
   ,"Ninetyfive_Five"
   ,"Ninety_Ten"
   ,"Convert"

]

points= {
    (1,1):(3,3),
    (1,0):(0,5),
    (0,1):(5,0),
    (0,0):(2,2),
}
def Fight(player1, player2,playto):
    repeat = 3
    avg_scores1 = 0
    avg_scores2 = 0
    FinalScore = ()
    for _ in range(repeat):
        List = []
        rounds = []
        history  = []
        p1 = []
        p1x = []
        p2 = []
        p2x = []

        print("while looping..")
        while len(history)<=playto:
            if isinstance(player1(1,history),list) == True:
                p1 = p1 +(player1(1,history))  
            else:
                p1 = p1 +[(player1(1,history))]  
            if isinstance(player2(2,history),list)==True:
                p2= p2 + (player2(2,history))
            else:
                p2= p2 + [player2(2,history)]

            history = []
            for tuple in zip(p1,p2):
                history.append(tuple)
        
            if len(p1)>len(p2):
                p1x = p1[1::1]
                for j in range(len(p1x)-1):
                    p2 = player2(2,history)
                    history.append((p1x[j],p2[-1]))
            elif len(p1)<len(p2):
                p2x = p2[1::1]
                for j in range(len(p2x)-1):
                    p1 = player1(1,history)
                    history.append((p1[-1],p2x[j]))


        p1points = 0
        p2points = 0
        history = history[:playto:]
        print("compiling..")
        for i in history:
            if i == (1,1):
                game = [("C","C"),points[i]]
                p1points += points[i][0]
                p2points += points[i][1]
            elif i == (1,0):
                game = [("C","D"),points[i]]
                p1points += points[i][0]
                p2points += points[i][1]            
            elif i == (0,1):
                game = [("D","C"),points[i]]
                p1points += points[i][0]
                p2points += points[i][1]            
            elif i == (0,0):
                game = [("D","D"),points[i]]
                p1points += points[i][0]
                p2points += points[i][1]  
            List.append(game)

        avg_scores1 += p1points
        avg_scores2 += p2points
    print("scoring..")          
    FinalScore = (round(avg_scores1/repeat),round(avg_scores2/repeat))
    print("creating final score..")
    return FinalScore


def RoundRobin(playerlist, playto):
    class Strategy:
        def __init__(self,averages):
            self.averages = averages

    FightsList=[]
    avglist = []
    for strat in playerlist:
        stratavg = 0
        for nstrat in playerlist:
            score = Fight(strat, nstrat, playto)
            stratavg += score[0]// len(playerlist)
        avglist.append((Player_dict[strat], stratavg))  
        #avglist.sort() 
        #Winner = avglist[0]    
    return avglist
    
    # return FightsList

def ClassicTourney(playerlist, playto, permutations):
    players = [strat for count,strat in enumerate(playerlist) if count != 2 and count != 22]
    Winners = [strat for count, strat in enumerate(playerlist) if count != 2 and count != 22]
    TourneyWinners = []
    while len(Winners)>1:
        print(Winners)
        players = [i for i in players if i in Winners]
        Winners = []
        for i in [num for num in range(len(players))if num%2 !=0]:
            if len(players) >= i +1:
                game = Fight(players[i],players[i+1],200)
            else:
                game = Fight(players[i],Tit_For_Tat,playto)
            if game[0]>game[1]:
                Winners.append(players[1])
            elif game[1]>game[0]:
                Winners.append(players[i+1])
            else:
                for avg in highest_avgs:
                    if Player_dict[players[i]] in avg:
                        Winners.append(players[i])
                        break
                    elif Player_dict[players[i+1]]in avg:
                        Winners.append(players[i+1])
    TourneyWinners.append(Winners)