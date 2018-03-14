# Roulette Martigan Calcultor V1.0
#
#  Jose Nunes - www.josenunes.co.nf
#
#  Espinho, Portugal 17/03/2016
#  python 2.x
#
import random

def getRouletteValue(doubleZero=False):
    """Return a random number like a roullette gamble machine,
    if the roullette has 2 zeros ('0' and '00') it return -1 in
    order to represent the value '00'. """
    if doubleZero==True:
        return random.randint(-1,36)
    return random.randint(0,36)

def play(money,initialBet,strategy,doubleZero=False):
    """Input: budget, initialBet, strategy, doubleZero
    Output: (boolean) true if strategy is acomplished,
    number of plays
    """
    #money=20
    maxMoney=money
    numPlays=0
    targetReached=False
    while(money>0):
        bet=initialBet
        while(bet<money):
            #print "lets bet: "+str(bet)
            ro=getRouletteValue(doubleZero)
            numPlays+=1
            #print "Roullette number: "+str(ro)
            if ro%2!=0 and ro>0:              #Condition where: Even number
                money+=bet
                if money>maxMoney:
                    maxMoney=money
                targetReached=False
                break
            else:
                money-=bet
                bet=2*bet
        if(bet>money):
        #print "game over"
            targetReached=False
            break
        if money>strategy:
            targetReached=True
            break
    #print "-------------------"
    #print "results:"
    #print "Money: "+str(money)
    #print "Max  : "+str(maxMoney)
    #print "Jogadas: "+str(njogadas)
    return targetReached, numPlays

def inputData():
    """Get information about budget, roullette type (minimum bet and type)
    and target and return """
    print "##############################"
    print "##                          ##"
    print "##   Roullette Martingale   ##"
    print "##     Simulator  V 1.0     ##"
    print "##                          ##"
    print "##############################"
    print '\n'
    budget=raw_input("Your Budget to bet: ")
    while budget<=0:
        print "Invalid input, please insert a valid monetary value!"
        budget=raw_input("Your new Valid Budget to bet: ")
    roulletteMinimumBet=raw_input("Roullette Minimum bet: ")
    while budget<=0:
        print "Invalid input, please insert a valid monetary value!"
        budget=raw_input("Your new Roullette Minimum: ")
    roulletteType=raw_input("Does the Roullette has 2 Zeros ('0' and '00'), Yes or No: ")
    while ( not roulletteType in ['y','Y','Yes','YES','yes','n','N','No','NO']):
        print "Invalid Input, type 'Yes' or 'No'"
        roulletteType=raw_input("Does the Roullette has 2 Zeros ('0' and '00'), Yes or No: ")
    if roulletteType in ['y','Y','Yes','YES','yes']:
        doubleZero=True
    else:
        doubleZero=False
    target=raw_input("Your target, how much do want to win: ")
    while target<roulletteMinimumBet:
        print "Invalid input, please insert a valid monetary value!"
    return budget, roulletteMinimumBet, roulletteType, target  

def outputData(targetReachedList,numPlaysList, budget, target):
    print "\n"
    print "Results:"
    print "Budget: "+str(budget)
    print "Target: "+str(target)
    print "Probabilty of Success: "+str( float(targetReachedList.count(True))/float(len(targetReachedList)) *100) + " %"
    print "Average number of Plays: "+str(sum(numPlaysList)/len(numPlaysList))



#Main program
budget, roulletteMinimumBet, doubleZero, target = inputData()         
targetReachedList=[]
numPlaysList=[]
for i in range(1000):
    targetReached, numPlays = play(budget,roulletteMinimumBet,target)
    targetReachedList.append(targetReached)
    numPlaysList.append(numPlays)
outputData(targetReachedList,numPlaysList, budget, target)    

    

