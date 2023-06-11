# Created by: Soren Atmakuri Davidsen
# Department of Computer Science at Sri Venkateswara University, Tirupati, INDIA
# email: sorend@cs.svu-ac.in
# GitHub Repository: <https://github.com/sorend/fylearn>

# Edited by: Sanket Patadiya
# SVNIT, Surat
# email: sanketsvnit03@gmail.com
# GitHub Repository: <https://github.com/sanket-03/Algorithmic-Analysis-of-One-Diode-PV-Model>

# Importing Required Libraries
from __future__ import print_function
import numpy as np
from fylearn.tlbo import TLBO, TeachingLearningBasedOptimizer
from fylearn.ga import helper_n_generations
import pytest


def oneDiode():
    
    # function to minimize - One Diode PV Model's Power Output
	def f(x):
		I, V     = x

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

	# Creating np.array object of lower and upper bounds
	lower_bounds = np.array([0, 0])
	upper_bounds = np.array([8.947, 44.71])

	# TLBO 
	tlbo = TLBO(f, lower_bounds, upper_bounds, n_population=15)
	tlbo = helper_n_generations(tlbo, 100)
	best_solution, best_fitness = tlbo.best()
	print("TLBO solution", best_solution, "fitness", best_fitness)

# Calling the function oneDiode 
oneDiode()

