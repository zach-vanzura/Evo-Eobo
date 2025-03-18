import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
print("this is when I finished evolution", os.path.exists("fitness*.txt"))
phc.Show_Best()
print("After showing best:", os.path.exists("fitness*.txt"))

