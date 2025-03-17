import os
from hillclimber import HillCLIMBER


hc = HillCLIMBER()
hc.Evolve()
hc.Show_Best()

# for i in range(5):
#     os.system("python3.11 generate.py")
#     os.system("python3.11 simulate.py")
