"""
File for simulate.py meant to keep track of constants
"""
import numpy as np

# max simulation run time
MAX_TIME = 500

# time step motors
motor_max_force = 50

# number of sensor and motor neurons
numSensorNeurons = 2
numMotorNeurons = 2

motorJointRange = 1.25 * np.pi

# number of generations for evolutionary alg
numberOfGenerations = 10

# population size for PARALLEL HILL CLIMBER
populationSize = 10
