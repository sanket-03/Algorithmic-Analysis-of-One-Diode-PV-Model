# Created by: Sanket Patadiya
# SVNIT, Surat (India)
# email: sanketsvnit03@gmail.com
# Dissertation Project: TLBO Algorithm based Analysis of Single-Diode Photovoltaic Model

# GitHub Repository: <https://github.com/sanket-03/Algorithmic-Analysis-of-One-Diode-PV-Model>

# Required Libraries
import random
import numpy as np

# The One Diode PV Model
    # equations 
        # I 	= I_ph - I_d - I_sh                                    
        # I_d	= I_0 * (math.exp((q*(V + (I * R_s)))/(m*k*T)) -1) ; Here I_d is `Diode Current`
        # I_sh = (V + (I * R_s)) / (R_sh) ; Here I_sh is `Shunt Current`

    # constants
        # q     - Electron charge magnitude [q = e = 1.6e-19]
        # K     - Boltmann constant         [k = 1.38e-23]
        # m     - Diode ideality factor     
        # R_s    - Series Resistance         
        # R_sh   - Shunt Resistance
        # Ki    - Current Temperature Coefficient
        # Kv    - Voltage Temperature Coefficient
        # n     - Number of cells in series
        # V_T   - Thermal Voltage Coefficient [V_T = K*q/T]
        # I_0    - Saturation Current 

    # variables
        # I - Load Current
        # V - Load Voltage

# Methodology

'''
    For the optimization of One Diode PV Model, this code uses TLBO (Teaching Learning based Optimisation) Approach.
    The TLBO Algorithm was proposed by R.V. Rao et. al. in the article 'Teaching–learning-based optimization: a novel method for constrained mechanical design optimization problems'.
    The link to the scientific paper - https://www.sciencedirect.com/science/article/pii/S0010448510002484

    For optimising the One Diode Model's equation to get the MPP (Maximum Power Point) we need to find Power (P) in terms of I (Current) and V (Voltage). 
    The formulas and definitions written at the start of this program will be considered for this code.
    In this approach I have created randomized population of `two` dimension as I and V are the two variables.
    As the code is written to find the `minima` for any function, I have multiplied all the Power values generated from One Diode model with `-1`.
    Detailed information about TLBO and it's working can be found in the above-mentioned paper.

'''

# Objective Function : Power output of One Diode Model
def one_diode_model(x, I_ph, I_0, n, R_s, R_sh):
    V       = x[0]
    I       = x[1]
    I_d     = I_0 * (np.exp((V + I * R_s) / (n * 1.65427)) - 1) # Diode Current - Shockley Diode Equation
    I_sh    = (V + I * R_s) / R_sh                              # Shunt Current
    Power   = (I_ph - I_d - I_sh)*V
    Power   = -Power  # As TLBO will work for minimization point
    return Power

# TLBO Function
# Inputs - Objective Function, Lower Bound, Upper Bound, Dimensions (2 : I, V), Maximum Iteration, Population Size
def tlbo(objective_func, lb, ub, dim, max_iter, pop_size): 

    # Initialize population
    population = np.zeros((pop_size, dim))
    for i in range(pop_size):
        population[i, :] = np.random.uniform(lb, ub, dim)

    # Main loop
    for _ in range(max_iter):
        '''
        # Teaching phase
        '''
        best_teacher_index = np.argmin([objective_func(x) for x in population])
        teacher = population[best_teacher_index, :]

        for i in range(pop_size):
            # Generate a new solution
            new_solution = population[i, :] + np.random.uniform(-1, 1, dim) * (teacher - population[i, :])

            # Check boundaries
            new_solution = np.clip(new_solution, lb, ub)

            # Compare with the current solution
            if objective_func(new_solution) < objective_func(population[i, :]):
                population[i, :] = new_solution

        '''
        # Learning phase
        '''
        for i in range(pop_size):
            # Select two random individuals
            r1, r2 = random.sample(range(pop_size), 2)

            # Generate a new solution
            new_solution = population[i, :] + np.random.uniform(-1, 1, dim) * (population[r1, :] - population[r2, :])

            # Check boundaries
            new_solution = np.clip(new_solution, lb, ub)

            # Compare with the current solution
            if objective_func(new_solution) < objective_func(population[i, :]):
                population[i, :] = new_solution

    # Find the best solution
    best_solution_index = np.argmin([objective_func(x) for x in population])
    best_solution = population[best_solution_index, :]

    return best_solution

# Main Function
def main():
    I_ph        = 8.949472665761322         # Photon Current - Due to Solar Irradiance
    I_0         = 6.9656760435636045e-09    # Diode Saturation current
    n           = 1.3                       # Diode ideality factor
    R_s         = 0.058                     # Series resistance
    R_sh        = 209.865                   # Shunt resistance
    lb          = [0, 0]                    # Lower bounds for V and I
    ub          = [44.71, 8.947]            # Upper bounds for V and I
    dim         = 2                         # Number of dimensions
    max_itr     = 500                       # Maximum number of iterations
    pop_size    = 15                        # Population size

    # Calling tlbo function
    best_solution = tlbo(lambda x: one_diode_model(x, I_ph, I_0, n, R_s, R_sh), lb, ub, dim, max_itr, pop_size)

    # Printing Output
    print("Best solution:", best_solution)
    print("Best objective value:", one_diode_model(best_solution, I_ph, I_0, n, R_s, R_sh))

# Executable Part    
if __name__ == '__main__':
    main()
