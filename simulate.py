import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)  # set to 0 to enable
p.setGravity(0,0,-9.8)
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

for i in range(10000):
    print(i)
    p.stepSimulation()
    time.sleep(1 / 60)


p.disconnect()
