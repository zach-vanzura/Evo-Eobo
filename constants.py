"""
File for simulate.py meant to keep track of constants
"""
import numpy as np

# max simulation run time
MAX_TIME = 500

# time step motors
time_step = np.linspace(0, 2 * np.pi, MAX_TIME)
motor_max_force = 100


# general constants for now...
amplitude = np.pi / 8
frequency = 60
phaseOffset = 0


# Constants for back leg
backLegAmplitude = np.pi / 8
backLegFrequency = 30
backLegPhaseOffset = 0

# constants for front leg
frontLegAmplitude = np.pi / 16
frontLegFrequency = 20
frontLegPhaseOffset = 2 * np.pi

# number of generations for evolutionary alg
numberOfGenerations = 10

