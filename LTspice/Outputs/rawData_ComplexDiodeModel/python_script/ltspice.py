'''
Created by: Sanket Patadiya
SVNIT, Surat (India)
email: sanketsvnit03@gmail.com
Dissertation Project: TLBO Algorithm based Analysis of Single-Diode Photovoltaic Model
 
GitHub Repository: <https://github.com/sanket-03/Algorithmic-Analysis-of-One-Diode-PV-Model>
'''

# This code calculates the values of Power (Pmax), Current (Imax) and Voltage (Vmax) at MPP for various illumination and temperature conditions from the ltspice complex diode model data 


# Importing required libraries
import pandas as pd
import os

# Edit with the path of your system's LTspice data directory
path = "[Path to LTspice Data Directory]"

# Change directory to the data directory
os.chdir(path)

# Iterating through all data files, please note the nomenclature of the data files is done as per below 
# File Name Nomenclature: [Temperature]_[Illumination] 
# Example: for 10 Kelvin temperature and 1000 Watts per sq.Meter illumination file name will be 10_1000.txt
for file in os.listdir():
    if file .endswith(".txt"):
        words = file.split('_')
        illu = words[0]
        temp = words[1].split('.')[0]
        data = pd.read_csv(file, sep="\t")

        # Creating list from the columns of the data
        time = data['time'].tolist()
        voltage = data['V(v+)'].tolist()
        current = data['I(I1)'].tolist()

        steps = len(time)
        
        # Calculating Power 
        power = []
        for i in range(steps):
            power.append(voltage[i]*current[i])
 
        # Finding MPP
        Pmax = max(power)
        i_max = power.index(Pmax)
        Vmax = voltage[i_max]
        Imax = current[i_max]
        
        # Printing Output
        print('---------------------------------------------')
        print('for illu = ', illu, "and temperature = ", temp)
        print('---------------------------------------------')
        print('Pmax', Pmax)
        print('Imax', Imax)
        print('Vmax', Vmax)
        print("\n")
