"""
many_epochs.py
Created by Zach Vanzura
CS 3060: Evolutionary robotics

run search n number of times,
save the data over each iteration to create an n sized array of pre-evolved robots for the future runs.
"""

import os
import constants as c


for e in range(c.numberOfEpochs):
    print("Epoch Number:", e)
    os.system("python3.11 search.py 1")
    if e == c.numberOfEpochs - 1:
        os.system("python3.11 search.py")

# most_fit_saved.txt
# TODO: With the saved data of each most fit child at each epoch, plot the trend of fitness
    # TODO: I will maybe want to also show the evolution of robots at individual epochs!
