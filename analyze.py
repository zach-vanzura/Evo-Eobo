import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('./data/backLegSensorValues.npy')
frontLegSensorValues = np.load('./data/frontLegSensorValues.npy')

sinValues = np.load('./data/sinValues.npy')

backLegMotorValues = np.load("./data/backLegMotorValues.npy")
frontLegMotorValues = np.load("./data/frontLegMotorValues.npy")

# print(backLegSensorValues)
# print(frontLegSensorValues)
# print(sinValues)

plt.plot(backLegMotorValues, linewidth=5, label='Back Leg')
plt.plot(frontLegMotorValues, label='Front Leg')
# plt.plot(sinValues, label='Target Values')
plt.legend()
plt.pause(10)
