import copy
import constants as c
import os
import pickle
from solution import SOLUTION

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        """
        in each generation of the PHC (which has multiple associated generations), we load the most fit data 
        from the previous generation if the aforementioned data exits
        """
        # load serialized and pickled data.
        if os.path.exists(c.pickle_file) and os.path.getsize(c.pickle_file) > 0:
            with open(c.pickle_file, 'rb') as pf:
                genotype = pickle.load(pf)
                for p in range(c.populationSize):
                    self.parents[p] = genotype[p]
                    self.nextAvailableID += 1
        # running PHC for first time, no data to latch on to
        else:
            for p in range(c.populationSize):
                self.parents[p] = SOLUTION(self.nextAvailableID)
                self.nextAvailableID += 1


    def Evolve(self):
        # evolve and evaluate each parent
        self.Evaluate(self.parents)
        for currentGen in range(c.numberOfGenerations):
            print("Current Generation: ", currentGen)
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
        self.parents[self.most_fit_key].Start_Simulation("GUI")

    def Save_Best(self):
        # pickle all final fitness for the next epoch
        with open(c.pickle_file, 'wb') as pf:
            pickle.dump(self.parents, pf)

        # find the best fit of the epoch
        self.most_fit = -1 * float('inf')  # set fitness to be as un-fit as possible
        for key in self.parents.keys():
            if self.parents[key].fitness > self.most_fit:
                self.most_fit = self.parents[key].fitness
                self.most_fit_key = key
        # save the best fit
        with open("most_fit_saved.txt", 'a') as f:
            f.write(str(self.parents[self.most_fit_key].fitness) + '\n')

    def Print(self):
        for i in self.parents.keys():
            print("")
            print(f"Fitness from parent {i}:", self.parents[i].fitness,
                  f"Fitness from Child {i}: ", self.children[i].fitness)
            print("")