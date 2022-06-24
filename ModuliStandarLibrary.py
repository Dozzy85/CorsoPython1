#Moduli

import os
os.getcwd()

import datetime
datetime.datetime.now

from time import time
from math import pow as power
import numpy as np

n = 2
pow = 10
n_pow = n
tick = time()
print(tick)
np_pow=np.power(n, n_pow)
duration = time()-tick
print(duration)