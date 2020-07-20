import math
#Finding the path loss with the help of COST 231 model
f=1900  # frequency is 1900 MHz
h=50  #height of base station is 50m

def path_loss(d):
    d1=d/1000  #distance in km
    pl=46.3+33.9*math.log10(f)-13.82*math.log10(h)+(44.9-6.55*math.log10(h))*math.log10(d1)
    return pl #path loss in dB
