
#IPD strats

#imports
import random
import time
import numpy as np

points= {
    (1,1):(3,3),
    (1,0):(0,5),
    (0,1):(5,0),
    (0,0):(2,2),
}

#Strategies

def Cooperator(player, score, modifiers = [None]):
    return [1]*200
def Defector(player, score, modifiers = [None]):
    return [0]*200
def Evil(player, score, modifiers = [None]):
    return [0,0,1,0,0]*40

def Random_Player(player,score,modifiers = [None]):
    return [random.choice([0,1])]
def Sixty_Forty(player, score, modifiers = [None]):
    return [random.choice([1,1,1,1,1,1,0,0,0,0])]
def Forty_Sixty(player, score, modifiers = [None]):
    return [random.choice([1,1,1,1,0,0,0,0,0,0])]
def Ninety_Ten(player, score, modifiers = [None]):
    return [random.choice([1,1,1,1,1,1,1,1,1,0])]
def Ten_Ninety(player, score, modifiers = [None]):
    return [random.choice([1,0,0,0,0,0,0,0,0,0])]
def Ninetyfive_Five(player, score, modifiers = [None]):
    return [random.choice([1]*95+[0]*5)]
def Five_Ninetyfive(player, score, modifiers = [None]):
    return [random.choice([0]*95+[1]*5)]

def Tit_For_Tat(player, score, modifiers = [None]):
    if score == []:
        return 1
    if player == 1:
        nprevious = score[-1][1]
    else:
        nprevious = score[-1][0]
    return [nprevious]
def twoTFT(player, score, modifiers = [None]):
    if len(score)==0:
        return 1
    if player == 1:
        nprevious = score[-1][1]
    else:
        nprevious = score[-1][0]
    if nprevious == 0:
        return [0,0]
    else:
        return [1]
def TFtwoT(player, score, modifiers = [None]):
    if len(score)>1:
        if player == 1:
            nprevious = score[-1][1]
            nprevious2 = score[-2][1]
        else:
            nprevious = score[-1][0]
            nprevious2 = score[-2][0]
        if nprevious & nprevious2 == 0:
            return [0]
        else:
            return [1]
    else:
        return [1]
def ForgivingTFT(player, score, modifiers = [None]):
    if len(score )==0:
        return 1
    if player == 1:
        nprevious = score[-1][1]
    else:
        nprevious = score[-1][0]
    if nprevious == 0:
        return [random.choice([0,0,0,0,0,0,0,0,0,1])]
    else: 
        return [1]
def susTFT(player, score, modifiers = [None]):
    if score == []:
        return [0]
    if player == 1:
        nprevious = score[-1][1]
    else:
        nprevious = score[-1][0]
    return [nprevious]
def ImperfectTFT(player, score, modifiers = [None]):
    if len(score )==0:
        return 1
    if player == 1:
        nprevious = score[-1][1]
    else:
        nprevious = score[-1][0]
    if nprevious == 1:
        invState = 0
    else:
        invState = 1
    return [random.choice([nprevious]*9+[invState])]
def Almost_Tit(player, score, modifiers = [None]):
    if len(score )==0:
        return 1
    if player == 1:
        nprevious = score[-1][0]
    else:
        nprevious = score[-1][1]
    if nprevious == 1:
        invState = 0
    else:
        invState = 1

    if nprevious == 0:  
        return [random.choice([nprevious]*9+[invState])]
    else:
        return [1]
def ProgressiveTFT(player, score,  modifiers = [None]):
    if len(score)==0:
        return [1]
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    nDcount = 1
    multiplier = nDcount
    for game in score:
        if game[opponent] == 0:
            nDcount += 1 
            multiplier = nDcount

    if score[-1][opponent] == 0:
        return [0]*multiplier 
    else:
        return [1]
def OmegaTFT(player, score, modifiers = [None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0

    if len(score) <3:
        return [1]
    
    if score[-1][opponent] == 0:
        return [0,0]
    if player == 0:
        nChoices5 = [i for i,j in [game for game in score]]
    else:
        nChoices5 = [i for h,i in [game for game in score]]
    if nChoices5 == [0,0,1,0,0]:
        return [0]
    else:
        return [1]
    
def Triggered(player, score, modifiers = [None]):
    triggered = False
    for game in score:
        if 0 in game:
            triggered = True
    if triggered == True:
        return [0]
    else:
        return [1]
def Convert(player, score, modifiers = [None]):
    converted = None
    for game in score:
        if 1 in game:
            converted = True
    if converted == True:
        return [1]
    else:
        return [0]
def ZeroDeterminant(player, score, modifiers =  [None]):
    if player == 1:
        pScores = [s[0] for s in score]
        nScores = [s[1] for s in score]
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
        pScores = [s[1] for s in score]
        nScores = [s[0] for s in score]        
    
    
    # Compute average scores
    p1_avg = np.mean(pScores)
    p2_avg = np.mean(nScores)
    
    # Compute covariance matrix
    cov_matrix = np.cov(pScores, nScores)
    
    # Compute determinant
    det = np.linalg.det(cov_matrix)
    
    # Determine ZD strategy
    if det == 0:
        # If determinant is 0, play Nice
        next_move = 1
    elif det < 0:
        if p1_avg < p2_avg:
            # If determinant is negative and p1_avg < p2_avg, play Extort-2
            next_move = 0
        else:
            # If determinant is negative and p1_avg >= p2_avg, play Extort-3
            next_move = 1
    else:
        # If determinant is positive, play Extort-1
        next_move = 0
        
    return [next_move]
def Sore_loser(player, score, modifiers = [None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    pscore = 0
    nscore = 0
    for game in score:
        if game[player] == 1 and game[opponent]== 1:
            pscore +=3 
            nscore +=3
        elif game[player] == 1 and game[opponent]== 0:
            nscore +=5
        elif game[player] == 0 and game[opponent]== 1:
            pscore += 5
        elif game[player] == 0 and game[opponent]== 0:
            pscore +=2 
            nscore +=2
    if pscore-nscore > 5:
        return [1]
    else:
        return [0]

def Behavioral_Pavlov(player, score, modifiers = [None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    nD_count = 0
    for game in score:
        if game[opponent] == 0:
            nD_count += 1 
    if nD_count%2 == 0:
        return [1]
    else:
        return [0]
def Quick_Pavlov(player, score, modifiers = [None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    if len(score) == 0:
        return [0,1,0,1]
    nChoices = []
    for count,game in enumerate(score):
        if count >4:
            break
        else:
            nChoices += [game[opponent]]
    
    if nChoices == [1,1,1,1]:
        return [score[-1][opponent]]
    elif nChoices == [0,0,0,0]:
        return[0]*196
    elif nChoices == [1,0,1,0]:
        return [score[-1][opponent]]
    elif nChoices == [1,0,0,0]:
        return[0]*196
    else:
        return [0]*196
def Adaptive_Pavlov(player,score,modifiers=[None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    if score ==[]:
        return [1]
    elif score[-1][player] == score[-1][opponent]:
        return [score[-1][player]]
    elif score[-1][opponent] < score[-1][player]:
        return [0]
    else:
        return [score[-1][player]]
def Safe_Palov(player, score, modifiers= [None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    if len(score)==0:
        return 1
    if len(score) <= 6:
        return [score[-1][opponent]]
    else:
        nChoices = []
        for num, game in enumerate([score]):
            if num >5:
                break
            else:
                nChoices += game[opponent]   
        if nChoices == [0,0,0,0,0,0]:
            return [0]*194
        elif nChoices == [111111]:
            return [score[-1][opponent]]
        elif score[1]== score[3] and score[3]== score[5] and score[1] ==score[5]:
            return [1]*194
        else:
            return [0]*194
def Gradual(player, score, modifiers = [None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    if len(score)==0:
        return [1]
    nCoop10 = [i for count,i in enumerate([game[opponent]for game in score]) if i!=0 and count <=10]
    if len(nCoop10) >6:
        return [1]
    else:
        return [score[-1][opponent]]
def Prober(player, score, modifiers = (None)):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    pDcount=[]
    if len(score)== 0:
        return [1]
    elif len(score)<= 2:
        return [random.choice([score[-1][opponent]]*10 + [1,0])]
    if score[-2][player] == 0 and score[-1][opponent]== 1 and score[-2][opponent]==1:
        return [0]
    else:
        return [random.choice([score[-1][opponent]]*10 + [1,0])]

def Probability(player,score,modifiers = [None]): 
    if len(score)!=0:
        if player == 1:
            player = 0
            opponent = 1
        else:
            player = 1
            opponent = 0
        nDchance = []
        for game in score:
            if game[opponent] == 0:
                nDchance.append(1)
            else:
                nDchance.append(0)
        return [random.choice(nDchance)]
    else:
        return [1]
def Grudger(player, score, modifiers = [None]):
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    nD_count = 0
    pD_count = 0
    for game in score:
        if game[player] == 0:
            pD_count += 1
        if game[opponent] == 0:
            nD_count += 1
    if nD_count > pD_count:
        return [0]
    else:
        return [1]   
def allC_then_Inverse(player, score, modifiers = [None]):
    
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0

    if len(score) <=100:

        return [1]
    else:
        return [i[opponent] for i in score[::-1]]
def Random_then_Inverse(player, score, modifiers = [None]):
    
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0

    if len(score) <=100:

        return [random.choice([0,1])]
    else:
        return [i[opponent] for i in score]
def Equalizer(player, score, modifiers = [None]):
    if len(score)==0:
        return 1
    if player == 1:
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    nScore = 0
    pScore = 0
    for game in score:
        pScore += points[game][player]
        nScore += points[game][opponent]

    if nScore > pScore:
        return [0]
    elif nScore <= pScore:
        return [1]  





#important lists 

Player_dict= {
    Cooperator:"Cooperator",
    Defector:"Defector",
    Evil:"Evil",
    Random_Player:"Random_Player",
    Sixty_Forty:"Sixty_Forty",
    
    Forty_Sixty:"Forty_Sixty",
    Ninety_Ten:"Ninety_Ten",
    Ten_Ninety:"Ten_Ninety",
    Ninetyfive_Five:"Ninetyfive_Five",
    Five_Ninetyfive:"Five_Ninetyfive",

    Tit_For_Tat:"Tit_For_Tat",
    twoTFT:"twoTFT",
    TFtwoT:"TFtwoT",
    ForgivingTFT:"ForgivingTFT",
    susTFT:"susTFT",

    ImperfectTFT:"ImperfectTFT",
    Almost_Tit:"Almost_Tit",
    ProgressiveTFT:"ProgressiveTFT",
    OmegaTFT:"OmegaTFT",
    Triggered:"Triggered",

    Convert:"Convert",
    ZeroDeterminant:"ZeroDeterminant",
    Sore_loser:"Sore_loser",
    Behavioral_Pavlov:"Behavioral_Pavlov",
    Quick_Pavlov:"Quick_Pavlov",

    Adaptive_Pavlov:"Adaptive_Pavlov",
    Safe_Palov:"Safe_Palov",
    Gradual:"Gradual",
    Prober:"Prober",
    Probability:"Probability",
    
    Grudger:"Grudger",
    allC_then_Inverse:"allC_then_Inverse",
    Random_then_Inverse:"Random_then_Inverse",
    Equalizer:"Equalizer",

}
Player_list = [
    key for key in Player_dict
]
