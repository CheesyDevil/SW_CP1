import random
import time
import math
import keyboard
#damage calculator function
def dmg(Pow, Con, Prs, Lck, Def, Agl, Mag=0):
    x=1
    rng=random.randint(1,250)
    if ((200+Con)+Prs)>=rng+Agl:#Hit
        rng=random.randint(1,250)
        if rng+((Prs*2)+(Lck/2))>=245:#Critical Hit
            x=1.5+(Prs/20)
        rng=random.randint(80,120)
        dmg=math.ceil((((Pow*x)-Def)+(Mag*x))*(rng/100))
        return dmg
    else:#Miss
        dmg=0
        return dmg
    
def playerturn():


#enemy turn function

#victory function
