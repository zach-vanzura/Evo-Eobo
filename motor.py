import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.MAX_TIME)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        if self.jointName == 'Torso_BackLeg':
            self.frequency = c.frequency / 2
        self.offset = c.phaseOffset
        self.values = (self.amplitude * np.sin(self.frequency * c.time_step + self.offset))

    def Set_Value(self, robot, time_step):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.values[time_step],
            maxForce=c.motor_max_force)

    def Save_Values(self):
        np.save(f"./data/{self.jointName}-motor-values.npy", self.values)

