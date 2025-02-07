import numpy as np
import matplotlib.pyplot as plt

backlegSensorValues = np.load('./data/backLegSensorValues.npy')

print(backlegSensorValues)

plt.plot(backlegSensorValues)
plt.show()
