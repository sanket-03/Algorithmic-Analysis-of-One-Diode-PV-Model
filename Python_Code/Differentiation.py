# Created by: Sanket Patadiya
# SVNIT, Surat (India)
# email: sanketsvnit03@gmail.com
# Dissertation Project: TLBO Algorithm based Analysis of Single-Diode Photovoltaic Model
 
# GitHub Repository: <https://github.com/sanket-03/Algorithmic-Analysis-of-One-Diode-PV-Model>

# Required Libraries
import random
import math

# The One Diode PV Model
    # equations 
        # I 	= Iph - Id - Ish                                    
        # Id	= I0 * (math.exp((q*(V + (I * Rs)))/(m*k*T)) -1) ; Here Id is `Diode Current`
        # Ish = (V + (I * Rs)) / (Rsh) ; Here Ish is `Shunt Current`

    # constants
        # q     - Electron charge magnitude [q = e = 1.6e-19]
        # K     - Boltmann constant         [k = 1.38e-23]
        # m     - Diode ideality factor     
        # Rs    - Series Resistance         
        # Rsh   - Shunt Resistance
        # Ki    - Current Temperature Coefficient
        # Kv    - Voltage Temperature Coefficient
        # n     - Number of cells in series
        # V_T   - Thermal Voltage Coefficient [V_T = K*q/T]
        # I0    - Saturation Current 
        
    # variables
        # I - Load Current
        # V - Load Voltage

# Methodology

'''
    Here, We have considered a resistive load (R_l) being offered at the receiving end of the One-Diode model.
    So, we can write V = I * R_l.
    By this way we can convert this problem into one variable problem.
    And, by differentiating the Power w.r.t V (Voltage) we get MPP (Maximum Power Point Value).
'''


# Constant Definitions 
K   = 1.38e-23    
q   = 1.6e-19
T   = 298.15
Ki  = 0.0005
Kv  = -0.0034
Rs  = 0.058
Rsh = 209.865
m   = 1.3

Voc = 44.71
Isc = 8.947

V_T = K*T/q
n   = Voc/0.7

I0  = (((Rs + Rsh)*Isc) - Voc) / (Rsh * math.exp((Voc)/(m*n*V_T))) 
Iph = Isc*((Rsh+Rs)/Rsh) 

Power = []
Current = []
Voltage = []
Power_dash = [] # Array to store values of Power differentiated by Voltage

v = 0   # Loop Initialisation
while v <= Voc:

    Id = I0*(math.exp(((v*Rs) + v)/(m*n*V_T)) - 1)  # Diode Current
    Ish = (((v*Rs) + v)/Rsh)                        # Shunt Current

    i = Iph - Id - Ish
    p = abs(i*v)
    
    Power.append(p)
    Current.append(i)
    Voltage.append(v)
    
    # Differentiation
    dId_dv = I0*(math.exp(((v*Rs) + v)/(m*n*V_T)))*((1+Rs)/(m*n*V_T))
    dIsh_dv = (1+Rs)/(Rsh)
    di_dv = - (dId_dv) - (dIsh_dv)
    dp_dv = (di_dv*v) + (i)
    
    Power_dash.append(abs(dp_dv))
    
    if i <= 0:
        break
    v += 0.1    # Loop Progression

# Fetching MPP
Pmax = max(Power)
i_max = Power.index(Pmax)
Vmax = Voltage[i_max]
Imax = Current[i_max]

# Printing MPP Values
print(f"At Maximum Power Point: \n Power = {Pmax} Watts, \n Voltage = {Vmax} Volts and  \n Current = {Imax} Ampere")

# Importing required libraries for graph plotting
import matplotlib.pyplot as plt
plt.title("Power - Voltage PV Curve based on One Diode Model")
plt.plot(Voltage, Power)
plt.plot([Vmax], [Pmax], marker="o", label=f'MPP\nPmax = {round(Pmax, 2)} W')
plt.text(Vmax-5, Pmax+10, '(Vmax = {} V, Imax = {} A)'.format(round(Vmax, 2), round(Imax, 2)))
plt.xlabel('Voltage (Volts)')
plt.ylabel('Power (Watts)')
plt.xlim([0,44.71])
plt.ylim([0,400])
plt.legend()
plt.grid()
plt.show()
