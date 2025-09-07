import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy.optimize import linprog
import warnings
warnings.filterwarnings("ignore")


class MakeBuyCalculator:
    """
    Comprehensive Make-vs-Buy Decision Calculator
    Implements: Break-even Analysis, NPV Analysis, Linear Programming
    """

    def __init__(self):
        self.results = {}

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

        # generate volume range of analysis
        volumes = np.linspace(volume_range[0], volume_range[1], 1000)

        # calculate costs using equations 4.1 and 4.2
        buy_costs = c_buy_f + c_buy_v * volumes   # Equation 4.1
        make_costs = c_make_f + c_make_v * volumes  # Equation 4.2

        # Determine decision logic based on equations 4.3-4.6
        decision_case = self._determine_decision_case(c_make_f, c_make_v, c_buy_f, c_buy_v)

        # calculate break-even point if applicable
        break_even_point = None

        if decision_case in ['case_2', 'case_3']:
            if abs(c_buy_v - c_make_v) > 1e-6:
                if decision_case == 'case_2':
                    # Case 2: x < (c_buy_f - c_make_f)/(c_make_v - c_buy_v)
                    if c_make_v > c_buy_v:  # ensure denominator is possitive
                        break_even_point = (c_buy_f - c_make_f) / (c_make_v - c_buy_v)

                else:
                    # Case 3: x > (c^make_f - c^buy_f) / (c^buy_v - c^make_v)  
                    if c_buy_v > c_make_v:  # Ensure denominator is positive
                        break_even_point = (c_make_f - c_buy_f) / (c_buy_v - c_make_v)