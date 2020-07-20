import random as rand
import math
import sys
import numpy as np
import location
import path_loss as pl
import fading as fad
import shadowing as sh
import rsl
import sinr

s_values=sh.shadow_array()  #creating and storing the shadowing values
counter=5
P_t=42  #power of transmitter is 42 dBm
G_t=12.1  #antenna gain is 12.1 dB
L=2.1  #line and connector losses are 2.1 dB
eirp_max=52  #eirp comes out to be 52 dBm(P_t+G_t-L)
eirp=52  #variable eirp
eirp_min=30  #eirp cannot fall below 30 dBm
c_max=56  #maximum number of available channels
c=7200  #counter for the number of channels in use
c_d=20  #maximum channels for admission control
c_i=15  #minimum channels for admission control
sinr_min=6  #required sinr value in dB
i=1
w=0
users=10000  #total number of available users
r_fail={}  #creating a dictionary for the users who fail the rsl test
active={}  #creating a dictionary for the users active on a call
r_min=-107  #minimum rsl level  is -107dBm
c_nr=0  #the counter for call attempts not counting retries
c_r=0  #the counter for call attempts including retries
b_c=0  #the counter for blocked calls due to channel capacity
b_s=0  #the counter for blocked calls due to signal strength
d_c=0  #the counter for dropped calls
f_c=0  #the counter for failed calls
s_c=0  #the counter for successfully completed calls
c_rad=[0,0]  #cell radius
c_p=0  #the counter for calls in progress at any given time

while i<= counter:
	#for cell radius if the user gets disconnected
	if c_rad[0] in active:
		pass
	else:
		c_rad[1]=0
		
	#checking on the active users dictionary
	list5=[]
	for k in active:
		if active[k][4]!=0:
			if active[k][2]!=0:
				active[k][2]-=1
				if active[k][3]>c_rad[1]:
					c_rad=[k,active[k][3]]
				f=fad.fading()
				r=rsl.rsl(active[k][0],active[k][1],f,eirp_max)
				sr=sinr.sinr(r,c_p)
				if sr<sinr_min:
					active[k][4]-=1
				else:
					active[k][4]=3
			if active[k][2]==0:
				s_c+=1
				c-=1
				list5.append(k)
		else:
			d_c+=1
			c-=1
			list5.append(k)

	#checking on the rsl test failed dictionary    
	list4=[]
	for l in r_fail:
		if r_fail[l][2]!=0:
			c_r+=1
			r_fail[l][2]-=1
			f=fad.fading()
			r=rsl.rsl(r_fail[l][0],r_fail[l][1],f,eirp)
			if r>=r_min:
				if c<c_max:
					c+=1
					c_d=math.ceil(np.random.exponential(60))  #generating a value exponentially distributed about mean(60 seconds)
					list2=[]
					list2=[r_fail[l][0],r_fail[l][1],c_d,r_fail[l][3],3]
					active[l]=list2
					r_fail[l][2]=0
				else:
					b_c+=1
					list4.append(l)
		if r_fail[l][2]==0:
			list4.append(l)
			b_s+=1

	#checking on the users who would attempt to make a call
	for j in range(users):
		a = rand.random()
		if a < 1/600:
			d=location.loc()
			p=pl.path_loss(d[0])
			f=fad.fading()
			s=sh.shadow_value(s_values,d[1],d[2])
			r=rsl.rsl(p,s,f,eirp)
			if r<r_min:
				list1=[]
				list1=[p,s,2,d[0]]
				w+=1
				r_fail['user' +repr(w)]=list1
			else:
				if c<c_max:
					c+=1
					c_d1=math.ceil(np.random.exponential(60))
					list3=[]
					list3=[p,s,c_d1,d[0],3]
					w+=1
					active['user' +repr(w)]=list3
				else:
					b_c+=1
			c_nr+=1
			c_r+=1
			
			
			
	#deleting values from dictionaries that are no longer required there
	for n in list5:
		if n in active:
			del active[n]

	for m in list4:
		if m in r_fail:
			del r_fail[m]
		
	users=10000-len(r_fail)-len(active)  #updating the number of users who would attempt to make a call again in the next second
	c_p=len(active)
	f_c=d_c+b_s+b_c
	# if i%120==0:
	print('The statistics for {} seconds are as follows: '.format(i))
	print('The number of call attempts not counting retries are: ',c_nr)
	print('The number of call attempts including retries are: ',c_r)
	print('The number of dropped calls are: ',d_c)
	print('The number of blocked calls due to signal strength are: ',b_s)
	print('The number of blocked calls due to channel capacity are: ',b_c)
	print('The number of successfully completed calls are: ',s_c)
	print('The number of calls in progress at any given time are: ', c_p)
	print('The number of failed calls (blocks + drops) are: ',f_c)
	print('The current cell radius is: ',c_rad[1])
	print('\n')

	#checking for admission control
	if c>c_d:
		eirp-=0.5  #decrease the eirp by 0.5dB
	elif c<c_i:
		eirp+=0.5  #increase the eirp by 0.5dB

	if eirp>eirp_max:
		eirp=eirp_max  #eirp cannot increase the max eirp
	elif eirp<eirp_min:
		eirp=eirp_min  #eirp cannot fall below 30dBm
	i=i+1
