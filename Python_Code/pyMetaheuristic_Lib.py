# Created by: Prof. Valdecy Pereira, D.Sc.
# UFF - Universidade Federal Fluminense (Brazil)
# email:  valdecy.pereira@gmail.com
# Lesson: pyMetaheuristic - Teaching Learning Based Optimization 
# GitHub Repository: <https://github.com/Valdecy>

# Edited by: Sanket Patadiya
# SVNIT, Surat
# email: sanketsvnit03@gmail.com
# GitHub Repository: <https://github.com/sanket-03/Algorithmic-Analysis-of-One-Diode-PV-Model>


# Required Libraries
import numpy as np

# TLBO
from pyMetaheuristic.algorithm import teaching_learning_based_optimization
from pyMetaheuristic.utils import graphs

# Target Function - It can be any function that needs to be minimize, However it has to have only one argument: 'variables_values'. This Argument must be a list of variables.
# For Instance, suppose that our Target Function is the Easom Function (With two variables x1 and x2. Global Minimum f(x1, x2) = -1 for, x1 = 3.14 and x2 = 3.14)

# Target Function: One Diode PV Model - Power Function 
def oneDiode(variables_values = [0, 0]):
    I, V     = variables_values

    # Constant Definitions

    K   = 1.38e-23  # Boltzmann Constant
    q   = 1.6e-19   # Electron charge magnitude
    T   = 298.15    # Operating Temperature (in kelvin)
    Rs  = 0.058     # Series Resistance
    Rsh = 209.865   # Shunt Resistance
    m   = 1.3       # Diode Ideality Factor
    Voc = 44.71     # Open Circuit Voltage
    Isc = 8.947     # Short Circuit Current
    V_T = K*T/q     # Thermal Voltage
    n   = Voc/0.7   # Number of cells in series

    # Diode Saturation Current
    I0  = (((Rs + Rsh)*Isc) - Voc) / (Rsh * np.exp((Voc)/(m*n*V_T)))
    
    # Photonic Current
    Iph = Isc * ((Rsh + Rs)/ Rsh) 

    # Diode Current - Shockley diode equation
    Id  = I0*(np.exp(((I*Rs)+V)/(m*n*V_T)) - 1)

    # Shunt Current
    Ish = ((V + (I*Rs))/ Rsh)

    # Power Function
    Power = (Iph - Id  - Ish)*V
    Power = -Power # As this is designed for minimisation, I have inverted the fuction to get minima

    return Power


# Target Function - Values
plt_params = {
   'min_values': (0, 0),
   'max_values': (8.947, 44.71),
   'step': (0.1, 0.1),
   'solution': [],
   'proj_view': '3D',
   'view': 'notebook'
}
graphs.plot_single_function(target_function = oneDiode, **plt_params)

# TLBO - Parameters
parameters = {
    'population_size': 15,
    'min_values': (0, 0),
    'max_values': (8.947, 44.71),
    'generations': 500,
    'verbose': True
}
# TLBO - Algorithm
tlbo = teaching_learning_based_optimization(target_function = oneDiode, **parameters)

# TLBO - Solution
variables = tlbo[:-1]
minimum   = tlbo[ -1]
print('Variables: ', np.around(variables, 4) , ' Minimum Value Found: ', round(minimum, 4) )

# TLBO - Plot Solution
plot_parameters = {
    'min_values': (0, 0),
    'max_values': (8.947, 44.71),
    'step': (0.1, 0.1),
    'solution': [variables],
    'proj_view': '3D',
    'view': 'notebook'
}
graphs.plot_single_function(target_function = oneDiode, **plot_parameters)

