import pandas as pd
import os

path = "/home/shivansh/The 4/In Process/Dissertation/code/LTspiceData"

os.chdir(path)

for file in os.listdir():
    if file .endswith(".txt"):
        words = file.split('_')
        illu = words[0]
        temp = words[1].split('.')[0]
        data = pd.read_csv(file, sep="\t")

        time = data['time'].tolist()
        voltage = data['V(v+)'].tolist()
        current = data['I(I1)'].tolist()

        steps = len(time)
        
        power = []
        for i in range(steps):
            power.append(voltage[i]*current[i])
 
        Pmax = max(power)
        i_max = power.index(Pmax)
        Vmax = voltage[i_max]
        Imax = current[i_max]
        print('---------------------------------------------')
        print('for illu = ', illu, "and temperature = ", temp)
        print('---------------------------------------------')
        print('Pmax', Pmax)
        print('Imax', Imax)
        print('Vmax', Vmax)
        print("\n")
