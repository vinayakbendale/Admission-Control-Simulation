import random as rand
import math
#Finding the co-ordinates of the user
def loc():
    ang1=rand.uniform(0,360)   #finding the angle
    ang=math.radians(ang1)  #converting into radians
    rad1=rand.uniform(0,100000000)  #finding the radius with the squared given radius
    rad=math.sqrt(rad1)  #taking the square root to scale it back according to the given radius
    x=rad*math.cos(ang)  #finding the x co-ordinate
    y=rad*math.sin(ang)  #finding the y co-ordinate
    dist=math.sqrt((x*x)+(y*y))  #assuming base-station at origin and applying distance formula
    d=[dist,x,y]
    return d  #distance in m
