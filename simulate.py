import numpy as np
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)  # set to 0 to enable
p.setGravity(0,0,-9.8)
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robot_id)

MAX_TIME = 100

backLegSensorValues = np.zeros(MAX_TIME)

for i in range(MAX_TIME):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1 / 60)

p.disconnect()

np.save("./data/backLegSensorValues.npy", backLegSensorValues)

print(backLegSensorValues)