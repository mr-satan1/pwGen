#!/usr/bin/env python
# Example of simple multiprocessing

import multiprocessing as mp
import random
import string
import os

# Define an output queue
outputQueue = mp.Queue()

# Define a function to process.
# In this case, lets generate a random 15 character passphrase.
def randomString(length, outputQueue):
    stringy = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(length))
    outputQueue.put(stringy)

# Set up a list of processes that we want to run
processes = [mp.Process(target=randomString, args=(15, outputQueue)) for x in range(10)]

# Execute processes 
for process in processes:
    process.start()

# Exit the completed proceeses

for process in processes:
    process.join()

# Get process results from output queue.
results = [outputQueue.get() for process in processes]
os.system('clear')
print "Here's some passwords:\n"
print "\n".join(results)
