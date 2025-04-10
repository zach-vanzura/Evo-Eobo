import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.MAX_TIME)

    def Get_Value(self, time_step):
        self.values[time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        return self.values[time_step]

    def Save_Values(self):
        np.save(f"./data/{self.linkName}-sensor-value", self.values)



