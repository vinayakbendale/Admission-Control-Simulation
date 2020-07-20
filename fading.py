import numpy as np
import math
#Finding the Rayleigh fading
def fading():
    fading1=np.random.rayleigh()
    fading=20*math.log10(fading1)  #fading in dB
    return fading
