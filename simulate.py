import math

import numpy as np
import pybullet as p
import pybullet_data
import random
import time
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)  # set to 0 to enable
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

MAX_TIME = 10000

backLegSensorValues = np.zeros(MAX_TIME)
frontLegSensorValues = np.zeros(MAX_TIME)

for i in range(MAX_TIME):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=random.randrange(-1, 2) * math.pi / 2.0,  # stop value is exclusive, steps are ints
        maxForce=100)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=random.randrange(-1, 2) * math.pi / 2.0,
        maxForce=100)
    time.sleep(1 / 60)

p.disconnect()

np.save("./data/backLegSensorValues.npy", backLegSensorValues)
np.save("./data/frontLegSensorValues.npy", frontLegSensorValues)

