import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import sys

try:
    many_epochs = sys.argv[1]
except IndexError:
    many_epochs= False


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Save_Best()
if not many_epochs:
    phc.Show_Best()

