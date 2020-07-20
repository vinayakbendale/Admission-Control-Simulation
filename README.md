# Admission-Control-Simulation


Python code for simulating admission control in a single cell cellular network. Admission Control is very important for CDMA systems. 

**Base station parameters**: 
- Basestation Height:  50 m
- Basestation Maximum Transmitter Power:  15.85 W = 42 dBm
- Line and Connector Losses: 2.1 dB
- Antenna Gain: 12.1 dB
- Carrier Frequency: 1900 MHz



**CDMA system parameters**:
- Carrier Bandwidth: 1.25 MHz
- Bit Rate: 12.5 kbps
- Processor Gain: 20 dB
- Noise Level: -110 dBm
- Required SINR: 6 dB
- Minimum Pilot RSL: -107 dBm
- Number of Available Traffic Channels: 56
- Maximum cell radius: 10 km

Users can appear anywhere within the 10 km radius with equal probability and try to make calls randomly during the simulation. 

Users appear at any time with equal probability (i.e. uniformly distrubed inside the circle) and are assumed to be stationary until the call ends.
Call lengths are exponentially distributed about the average call duration. 

- Call Arrival Rate: λ= 6 calls per hour
- Average Call Duration: 1 minute
- Number of Users: 1000

The simulation is to run for 2 hours with time step increments of 1 second. 

Path Loss (PL) is modeled using COST-231 model turned for a small city, (Cm = 0 and a(hm) = 0).

Received Signal Level (RSL) = EIRP - PL + S + F

where, PL is path loss - calculated by COST-231 model
S - shadowing
F - Fading


Shadowing values are found using Log-Normal distribution with 0 db mean and SD of 2 dB<sup>2</sup>. Shadowing values are independent of time, so they are calculated only once at the start of for each 10m by 10m squares in the circle.

Fading values are obtained for every second using Rayleigh Distribution. 
    F = 20 * log<sub>10</sub>x, where x is the Rayleigh value.
    
Signal Level = RSL + System Processor Gain

Interference Level = RSL + 10 * log<sub>10</sub>(N-1), where N = number of users on the cell
