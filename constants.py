"""
File for simulate.py meant to keep track of constants
"""
import numpy as np

# max simulation run time
MAX_TIME = 1000

# time step motors
time_step = np.linspace(0, 2 * np.pi, MAX_TIME)

# general constants for now...
amplitude = np.pi / 4
frequency = 20
phaseOffset = 0


# Constants for back leg
backLegAmplitude = np.pi / 4
backLegFrequency = 20
backLegPhaseOffset = 0

# constants for front leg
frontLegAmplitude = np.pi / 4
frontLegFrequency = 20
frontLegPhaseOffset = 0.4 * np.pi

