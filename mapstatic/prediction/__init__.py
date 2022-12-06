#importing modules
import os
from  import *
from .meanmethod.datadownloading import datadownloading
from .meanmethod.datashaping import datashaping
from .meanmethod.datamodeling import prediction
from statsmodels.tools.eval_measures import rmse
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
