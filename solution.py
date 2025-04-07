import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random as r
import time

class SOLUTION:
    def __init__(self, availableID):
        self.myID = availableID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)  # random 3 X 2 rand array
        self.weights = 2 * self.weights - 1


    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python3.11 simulate.py " + directOrGUI + f" {self.myID}" + " 2&>1")

    def Wait_For_Simulation_To_End(self):
        # allow for the program to create the necessary fitness.txt file for the robot
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)

        with open(f"fitness{self.myID}.txt", 'r') as f:
            self.fitness = float(f.read())

        os.system(f"rm fitness{self.myID}.txt")

    def Set_ID(self, availableID):
        self.myID = availableID


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # creating torso and arms, all with absolute positions

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.8], size=[1, 0.5, 1.6])

        pyrosim.Send_Joint(name="Torso_LeftArm", parent="Torso", child="LeftArm", type="revolute",
                           position=[-0.125, 0, 1.2], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="LeftArm", pos=[-0.5, 0, 0.8], size=[0.25, 0.25, 1.6])

        pyrosim.Send_Joint(name="Torso_RightArm", parent="Torso", child="RightArm", type="revolute",
                           position=[0.125, 0, 1.2], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="RightArm", pos=[0.5, 0, 0.8], size=[0.25, 0.25, 1.6])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="LeftArm")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="RightArm")

        pyrosim.Send_Motor_Neuron(name=2, jointName="Torso_LeftArm")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_RightArm")


        for currentRow in range(c.numSensorNeurons):  # iterate over names of sensor neurons
            for currentCol in range(c.numMotorNeurons):  # iterate over names of motor neurons
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentCol + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentCol])

        pyrosim.End()

    def Mutate(self):
        rand_row = r.randint(0, c.numSensorNeurons - 1)  # minus ones are accounting for 0 indexing
        rand_col = r.randint(0, c.numMotorNeurons - 1)
        self.weights[rand_row][rand_col] = 2 * r.random() - 1





