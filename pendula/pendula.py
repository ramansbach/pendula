import numpy as np
import pandas as pd
import scipy.optimize as opt
from scipy.special import erf


__all__ = ["Pendulum"]


class Pendulum:
    
    def __init__(self):
        print("I am a pendulum")
        
    def eqns_of_motion(self):
        print("we are the equatiosn of motion")
        
    def simulate(self):
        print("simulate me!")

    def savedata(self):
        print("save your data")
        
    def dummytest(self):
        return True