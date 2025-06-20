# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
import random

from scipy import stats

def check ( squad_a , squad_b ):
    if ( len(squad_b) * len(squad_a) == 0 ):
        print('Check Error: A or B is empty')
        return('X')
    
def wound ( ww , squad ):
    if ( len(squad) == 0 ):
        print('Wound Error: target squad is empty')
        return('X')
    else:
        w=ww[1]
        for obj in squad: 
            while(w>0):
                obj.W -= 1
                w -= 1
                if (obj.W==0):
                    break   
        i=len(squad)-1
        l=len(squad)
        kills = 0
        while ( i>-1 ):
            if (squad[i].W==0):
                kills = kills +1
                del squad[i]
            i-=1
        #print('Killed' , kills , '/' , l , 'Units')
        return (kills)



def melee ( squad_a , squad_b ):

    if ( len(squad_b) * len(squad_a) == 0 ):
        print('Melee Error: A or B is empty')
        return('X')
    
    Atot=0
    for obj in squad_a: 
        Atot = Atot + obj.A

    WSdiff = squad_a[0].WS-squad_b[0].WS
    Hit = 4 - WSdiff
    if (Hit > 6):
        Hit = 6
    if (2 > Hit):
        Hit = 2
    WOdiff = squad_a[0].S-squad_b[0].T
    Wou = 4 - WOdiff
    if (Wou > 6):
        Wou = 6
    if (2 > Wou):
        Wou = 2

    #print(Hit , Wou)
    
    Hittotal = 0
    for a in range(0, Atot):
        x=random.randrange(6)+1
        if (x >= Hit ):
            #print('hit' , x)
            Hittotal = Hittotal +1
        #else: (print('miss' , x))
    Woundtotal = 0
    for b in range(0, Hittotal):
        y=random.randrange(6)+1
        if (y >= Wou ):
            #print('wound' , y)
            Woundtotal = Woundtotal +1
        #else: print('fail' , y)
    return (Hittotal , Woundtotal)


def shoot ( squad_a , squad_b ):

    if ( len(squad_b) * len(squad_a) == 0 ):
        print('Shoot Error: A or B is empty')
        return('X')
    
    Atot=0
    for obj in squad_a: 
        Atot = Atot + obj.Awep
    
    BSdiff = squad_a[0].BS - coverB
    Hit = BSdiff
    if (Hit > 6):
        Hit = 6
    if (1 > Hit):
        Hit = 1
    WPdiff = squad_a[0].Swep-squad_b[0].T
    WPu = 4 - WPdiff
    if (Wou > 6):
        Wou = 6
    if (2 > Wou):
        Wou = 2

    #print(Hit , Wou)
    
    Hittotal = 0
    for a in range(0, Atot):
        x=random.randrange(6)+1
        if (x >= Hit ):
            #print('hit' , x)
            Hittotal = Hittotal +1
        #else: print('miss' , x))
    Woundtotal = 0
    for b in range(0, Hittotal):
        y=random.randrange(6)+1
        if (y >= Wou ):
            #print('wound' , y)
            Woundtotal = Woundtotal +1
        #else: print('fail' , y)
    return (Hittotal , Woundtotal)


class Unit:
  def __init__(self, WS, BS, S, T, W, A, Ld, Ar, Sv):
    self.WS = WS
    self.BS = BS
    self.S = S
    self.T = T
    self.W = W
    self.A = A    
    self.Ld = Ld
    self.Ar = Ar
    self.Sv = Sv

#INIT

squad_1 = []
squad_2 = []
#                       (WS, BS, S, T, W, A, Ld, Ar, Sv)
for i in range(0 , 1):
    squad_1.append( Unit( 8, 1, 7, 7, 3, 7, 9, 1, 5))
for i in range(0 , 100):
    squad_2.append( Unit( 3, 3, 3, 3, 1, 1, 5, 6, 7))


#BEGIN
    
#random.shuffle(deck)
A=0
runs = 1000000
attack_commands=10
remaining=0

for m in range(1, runs):
    #for i in range(m):
#Re-init   
        squad_2 = []
        for j in range(0 , 100):
            squad_2.append( Unit( 3, 3, 3, 3, 1, 1, 5, 6, 7))
#number of attack commands               
        for k in range(attack_commands):
            
            if (check( melee (squad_1 , squad_2) , squad_2 ) == 'X'):
                print('break at attack number ' , k)
                break
            else:
                wound( melee (squad_1 , squad_2) , squad_2 )
        #print(remaining)
        #print( len(squad_2) , ' Survived the manslaughter in run ' , m)
        remaining=remaining+len(squad_2)
        #print(100-y ,'#' , 100-70*25/36 )
print(remaining/runs , 100-70*25/36 )


#for obj in squad_2:
#    print( obj.W, sep =' ' )

#DATA

#for i in range (5):
#    deck = MixandSplit ( deck )

#data = []
#for i in range(10000):
   # random.shuffle(deck)
   # data.append(Entropy(deck))


#data = np.sort(data)
#meam = np.mean(data)
#sigma = np.std(data)


#plt.plot(data)
#plt.show()

#fig, ax = plt.subplots(figsize=(8, 4))


#ax.hist(data, bins=1000, density=True)
#ax.plot(data, pdf_lognorm)
#ax.set_ylabel('probability')
#ax.set_title('Linear Scale')
#plt.show()




#for obj in deck: 
#    print( obj.suit, obj.value, sep =' ' )

