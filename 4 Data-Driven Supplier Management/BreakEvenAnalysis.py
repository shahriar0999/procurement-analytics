import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy.optimize import linprog
import warnings
warnings.filterwarnings("ignore")


def break_even_analysis(self, c_make_f, c_make_v, c_buy_f, c_buy_v, volume_range=(0, 20000)):
        """
        Perform break-even analysis for make vs buy decision using equations 4.1-4.6

        Parameters:
        - c_make_f: Fixed cost for make option
        - c_make_v: Variable cost per unit for make option
        - c_buy_f: Fixed cost for buy option 
        - c_buy_v: Variable cost per unit for buy option
        - volume_range: Range of volumes to analyze
        """