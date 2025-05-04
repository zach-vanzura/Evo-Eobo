"""
many_epochs.py
Created by Zach Vanzura
CS 3060: Evolutionary robotics

run search n number of times,
save the data over each iteration to create an n sized array of pre-evolved robots for the future runs.
"""

import os
import constants as c

if os.path.exists('previous_epoch_pickled.pkl') and os.path.getsize('previous_epoch_pickled.pkl') > 0:
    os.system("python3.11 search.py")  # show best from pre evolved population

for e in range(c.numberOfEpochs):
    print("Epoch Number:", e)
    if e == c.numberOfEpochs - 1:
        os.system("python3.11 search.py")
    else:
        os.system("python3.11 search.py 1")  # don't show best at the end of search runtime

# most_fit_saved.txt
# TODO: With the saved data of each most fit child at each epoch, plot the trend of fitness
    # TODO: I will maybe want to also show the evolution of robots at individual epochs!
