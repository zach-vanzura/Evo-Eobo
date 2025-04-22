"""
File for simulate.py meant to keep track of constants
"""
import numpy as np

# max simulation run time
MAX_TIME = 1000

# time step motors
motor_max_force = 175

# number of sensor and motor neurons
numSensorNeurons = 4
numMotorNeurons = 4

# body part lengths proportional to torso length
torso_length = 1.6
arm_length = torso_length * 1.15
leg_length = torso_length * 1.2

# body part heights, again proportional to torso length and leg length
torso_height = (torso_length * 0.5) + leg_length
shoulder_height = torso_length + leg_length  # shoulders at the top of the torso
hip_height = leg_length  # hips at the top of the legs (bottom of the torso!)
arm_height = arm_length * 0.5  # arms start at shoulders and go down
leg_height = -hip_height * 0.5  # legs below hips

motorJointRange = .5 * np.pi

# number of generations for evolutionary alg
numberOfGenerations = 50

# population size for PARALLEL HILL CLIMBER
populationSize = 20
