#Calculating the RSL value
def rsl(p,s,f,eirp):
    r=eirp-p+s+f  #computed rsl in dBm
    return r
