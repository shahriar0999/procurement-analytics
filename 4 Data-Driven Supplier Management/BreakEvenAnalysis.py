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

        # store results
        self.results['breakeven'] = {
            'c_make_f': c_make_f,
            'c_make_v': c_make_v,
            'c_buy_f': c_buy_f,
            'c_buy_v': c_buy_v,
            'volumes': volumes,
            'make_costs': make_costs,
            'buy_costs': buy_costs,
            'break_even_point': break_even_point,
            'decision_case': decision_case,
            'cost_estimation': {
                'buy': f"c_buy = {c_buy_f} + {c_buy_v} * x",
                'make': f"c_make = {c_make_f} + {c_make_v} * x"
            }
        }
    
    def _determine_decision_case(self, c_make_f, c_make_v, c_buy_f, c_buy_v):
        """
        Determine which decision case applies based on equations 4.3-4.6
        """
        
        # Case 1: Always MAKE (Equation 4.3)
        if c_make_f <= c_buy_f and c_make_v <= c_buy_v:
            return 'case_1_always_make'
        
        # Case 2: MAKE if quantity is small (Equations 4.4-4.5) 
        elif c_make_f <= c_buy_f and c_make_v > c_buy_v:
            return 'case_2'
            
        # Case 3: MAKE if quantity is large (Equation 4.6)
        elif c_make_f > c_buy_f and c_make_v < c_buy_v:
            return 'case_3'
            
        # Case 4: Always BUY
        else: # c_make_f > c_buy_f and c_make_v >= c_buy_v
            return 'case_4_always_buy'
        

        
