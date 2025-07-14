#iterated prisoner s dillema AI

#VARS and files
import time
import random
import pygame
import numpy as np
from itertools import combinations as cb

from IPDStrategies import  Cooperator ,  Defector ,  Evil ,  Random_Player ,  Sixty_Forty ,  Forty_Sixty ,  Ninety_Ten ,  Ten_Ninety ,  Ninetyfive_Five ,  Five_Ninetyfive ,  Tit_For_Tat ,  twoTFT ,  TFtwoT ,  ForgivingTFT ,  susTFT ,  ImperfectTFT ,  Almost_Tit ,  ProgressiveTFT ,  OmegaTFT ,  Triggered ,  Convert ,  ZeroDeterminant ,  Sore_loser ,  Behavioral_Pavlov ,  Quick_Pavlov ,  Adaptive_Pavlov ,  Safe_Palov ,  Gradual ,  Prober ,  Probability ,  Grudger ,  allC_then_Inverse ,  Random_then_Inverse ,  Equalizer 
from IPDStrategies import Player_list
from IPD_Simulations import RoundRobin, ClassicTourney



#stats
def Analysis():
    pass
def Isolate_means(scores):
    Means = []
    tempdict = {j:i for i,j in scores}
    print(tempdict)
    unsorted = []
    for key in tempdict:
        unsorted.append(key)
    sortd = sorted(unsorted)
    print(sortd)
    for key in sortd[::-1]:
        print(tempdict[key])
        Means.append(tempdict[key])
#display



#RUN
ClassicTourney(Player_list,200,4)


