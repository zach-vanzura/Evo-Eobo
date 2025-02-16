import math
import matplotlib.pyplot as plt
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

MAX_TIME = 1000

backLegAmplitude = np.pi / 4
backLegFrequency = 20
backLegPhaseOffset = 0

frontLegAmplitude = np.pi / 4
frontLegFrequency = 20
frontLegPhaseOffset = 0.4 * np.pi

backLegSensorValues = np.zeros(MAX_TIME)
frontLegSensorValues = np.zeros(MAX_TIME)
backLegMotorValues = np.zeros(MAX_TIME)
frontLegMotorValues = np.zeros(MAX_TIME)

x = np.linspace(0, 2 * np.pi, MAX_TIME)
backLegTargetAngles = np.array(backLegAmplitude * np.sin(backLegFrequency * x + backLegPhaseOffset))
frontLegTargetAngles = np.array(frontLegAmplitude * np.sin(frontLegFrequency * x + frontLegPhaseOffset))
# np.save("./data/sinValues.npy", targetAngles)

for i in range(MAX_TIME):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    backLegMotorValues[i] = backLegTargetAngles[i]
    frontLegMotorValues[i] = frontLegTargetAngles[i]
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegTargetAngles[i],  # stop value is exclusive, steps are ints
        maxForce=100)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegTargetAngles[i],  # stop value is exclusive, steps are ints
        maxForce=100)

    time.sleep(1 / 60)

p.disconnect()

np.save("./data/backLegSensorValues.npy", backLegSensorValues)
np.save("./data/frontLegSensorValues.npy", frontLegSensorValues)
np.save("./data/backLegMotorValues.npy", backLegMotorValues)
np.save("./data/frontLegMotorValues.npy", frontLegMotorValues)

