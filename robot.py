import constants as c
from motor import MOTOR
import os
import pyrosim.pyrosim as pyrosim
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR


class ROBOT:
    def __init__(self, solutionID):
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system(f"rm brain{solutionID}.nndf")
        self.left_val = 0
        self.right_val = 0
        self.both_on_floor = 0

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, time_step):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(time_step)  # this is wrong!
            val = self.sensors[linkName].values[time_step]
            if linkName == 'LeftArm':
                self.left_val = val
            if linkName == 'RightArm':
                self.right_val = val
        if self.left_val == 1 and self.right_val == 1:
            self.both_on_floor += 1


    def Think(self):
        self.nn.Update()


    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, time_step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Get_Fitness(self, solutionID):
        self.basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        self.basePosition = self.basePositionAndOrientation[0]
        self.xyPosition = abs(self.basePosition[1] - self.basePosition[0])
        self.zPosition = self.basePosition[2]

        on_floor_ratio = self.both_on_floor / c.MAX_TIME
        torso_bottom_Z = self.zPosition - c.torso_height / 2
        with open(f"tmp{solutionID}.txt", 'w') as f:
            f.write(str(on_floor_ratio))

        os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")


