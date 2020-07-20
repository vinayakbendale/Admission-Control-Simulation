import numpy as np
import math
#Finding the shadowing values
l=2000  #since the radius of the cell is 10km, diameter = 20,000m
z=[]
def shadow_array():
    for i in range(l):
        z.append([])
        for j in range(l):
            x=np.random.normal(0,2)  #the shadowing value in a particular square
            z[i].append(x)  #creating a 2000x2000 array with randomly assigned values
    return z

def shadow_value(z,x,y):
    x1=x+10000  #shifting the x co-ordinate in accordance with the 2d array since the origin was assumed to be at the base station
    y1=y+10000  #shifting the y co-ordinate in accordance with the 2d array since the origin was assumed to be at the base station
    x2=x1/10  #dividing by 10 since each square is of 10m x 10m
    y2=y1/10  #dividing by 10 since each square is of 10m x 10m
    a=math.floor(x2)  #working on the x co-ordinate to get to the proper indexing
    b=math.floor(y2)  #working on the y co-ordinate to get to the proper indexing
    l=z[a][b]  #final shadowing value
    return l
