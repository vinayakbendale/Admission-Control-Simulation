import math
#Calculating the SINR value
def sinr(rsl,n):
    if n==1:
        inter=0  #interference in linear scale
        noise1=-110  #noise level in dBm
        noise=(math.pow(10,noise1/10))*0.001  #computing noise in linear scale
        x1=noise+inter
        x=10*math.log10(x1)  #converting the above calculated sum into dB
        p_g=20  #processor gain is 20 dB
        s_l1=rsl+p_g  #signal level in dBm
        s_l2=math.pow(10,s_l1/10)*0.001  #converting signal level in linear scale
        s_l=10*math.log10(s_l2)  #computing signal level in dB
        sinr=s_l-x  #sinr level in dB
    else:
        inter1=rsl+10*math.log10(n-1)  #finding the interference level in dBm
        inter=math.pow(10,inter1/10)*0.001  #converting interference in linear scale
        noise1=-110  #noise level in dBm
        noise=(math.pow(10,noise1/10))*0.001  #computing noise in linear scaleinter=math.pow(10,inter1/10)  #converting interference in linear scale
        x1=noise+inter
        x=10*math.log10(x1)  #converting the above calculated sum into dB
        p_g=20  #processor gain is 20 dB
        s_l1=rsl+p_g  #signal level in dBm
        s_l2=math.pow(10,s_l1/10)*0.001  #converting signal level in linear scale
        s_l=10*math.log10(s_l2)  #computing signal level in dB
        sinr=s_l-x  #sinr level in dB
    return sinr
