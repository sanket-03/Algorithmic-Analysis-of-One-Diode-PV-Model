# Created by: Sanket Patadiya
# SVNIT, Surat (India)
# email: sanketsvnit03@gmail.com
# Dissertation Project: TLBO Algorithm based Analysis of Single-Diode Photovoltaic Model
 
# GitHub Repository: <https://github.com/sanket-03/Algorithmic-Analysis-of-One-Diode-PV-Model>

# Import required python modules and libraries
import random 
import numpy as np
import math

# The One Diode PV Model
    # equations 
        # I 	= I_ph - I_d - I_Rsh                                    
        # I_d	= I_0 * (np.exp((q*(V + (I * R_s)))/(m*k*Temp)) -1) ; Here I_d is `Diode Current`
        # I_Rsh = (V + (I * R_s)) / (R_sh) ; Here I_Rsh is `Shunt Current`

    # constants
        # q     - Electron charge magnitude [q = e = 1.6e-19]
        # k     - Boltmann constant         [k = 1.38e-23]
        # m     - Diode ideality factor     
        # R_s   - Series Resistance         
        # R_sh  - Shunt Resistance
        # I_0   - Saturation Current 
    
    # parameters
        # Temp  - Temperature 
        # I_ph  - Photonic Current / Illumination 

    # variables
        # I - Load Current
        # V - Load Voltage

# Methodology

'''
    Here, We have considered a resistive load (R_l) being offered at the receiving end of the One-Diode model.
    So, we can write V = I * R_l.
    By this way we can convert this problem into one variable problem.
'''

# Constants
q 	    = 1.6e-19
k 	    = 1.380649e-23
m 	    = 1.3
R_s 	= 0.058
R_sh 	= 209.865
V_oc    = 44.71     # Open Circuit Voltage
I_sc    = 8.947     # Short Circuit Current
n       = V_oc/0.7  # Number of cells in series

# Array Initiation
Voltage = []
Current = []
Power = []


Temp = 273

for _ in range(6):      # Iterating for 6 different Temperature values (273 K, 283 K, 293 K, 303 K, 313 K, 323 K)
    
    V_T	= (k*(Temp + 273.15))/q     # V_T is Thermal Voltage, it is a constant quantity for particular Temperature

    current = []
    voltage = []
    power = []

    V = 0   # Initialising Loop (from V = 0 it will vary till V = Open circuit voltage value i.e. V_oc)
    while V <= V_oc:

        voltage.append(V)
        I_0     = (((R_s + R_sh)*I_sc) - V_oc) / (R_sh * np.exp((V_oc)/(m*n*V_T)))     # Saturation Current
        I_ph    = I_sc * ((R_sh + R_s)/ R_sh)                                          # Photonic Current

        # V = I * R_l and R_l = 1 
        I_d     = I_0 *(np.exp((q*(V + (V*R_s)))/(n*m*k*Temp)) - 1)                             # Diode Current
        I_Rsh   = (V + (V*R_s)) / (R_sh)
        I       = I_ph - I_d - I_Rsh

        current.append(I)
        power.append(abs(I*V))
        V += 0.1

    Current.append(current) 
    Voltage.append(voltage)
    Power.append(power)
    Temp += 10
    

# importing pyplot package from matplotlib for plotting curve

import matplotlib.pyplot as plt

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.plot(Voltage[i], Current[i])
    plt.title(f"Temperature = {(i*10)+273} Kelvin")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.xlim(0, 44.71)
    plt.grid()

plt.suptitle("Characteristic Curve - One Diode PV Model ")
plt.show()

for i in range(6):
    plt.plot(Voltage[i], Current[i], label = f"{i*10 + 273} K" )
    plt.title(f"Characteristic Curve - One Diode PV Model")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.xlim(0, 44.71)

plt.legend(title = "Temperature (Kelvin)")
plt.grid()
plt.show()

