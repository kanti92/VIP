"""
This library contains all those classes to load, process and generate the data in VIP. 

- load_cube.py --> ...

- synthetic_data.py --> ...

- data_augmentation.py --> ...

- injection.py --> ...

- specifications.py --> ...

Astronomical calibration functionality like flat fielding and dark-sky
subtraction, in spite of its simplicity was not included in VIP because of the
heterogeneity of the datasets coming from different observatories (each having
different data storage and headers). You can perform this in python in
procedures of a few lines or using dedicated instrument pipelines such as
esorex (ESO instruments).
"""

from load_cube import *
from synthetic_data import *
from data_augmentation import *
from injection import *
from specifications import *


