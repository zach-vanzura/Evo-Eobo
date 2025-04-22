import copy
import constants as c
import os
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for p in range(c.populationSize):
            self.parents[p] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        # evolve and evaluate each parent
        self.Evaluate(self.parents)
        for currentGen in range(c.numberOfGenerations):
            print("Generation Number:", currentGen)
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness < self.children[key].fitness:  # child out competes parent (?)
                self.parents[key] = self.children[key]

    def Show_Best(self):
        self.most_fit = -1 * float('inf')  # set fitness to be as un-fit as possible
        for key in self.parents.keys():
            if self.parents[key].fitness > self.most_fit:
                self.most_fit = self.parents[key].fitness
                self.most_fit_key = key
        self.parents[self.most_fit_key].Start_Simulation("GUI")


    def Print(self):
        for i in self.parents.keys():
            print("")
            print(f"Fitness from parent {i}:", self.parents[i].fitness,
                  f"Fitness from Child {i}: ", self.children[i].fitness)
            print("")