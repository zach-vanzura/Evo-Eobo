import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('./data/backLegSensorValues.npy')
frontLegSensorValues = np.load('./data/frontLegSensorValues.npy')

print(backLegSensorValues)
print(frontLegSensorValues)

plt.plot(backLegSensorValues, linewidth=3, label='Back Leg')
plt.plot(frontLegSensorValues, label='Front Leg')
plt.legend()
plt.show()
