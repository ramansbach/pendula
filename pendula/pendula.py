import numpy as np
import pandas as pd
import scipy.optimize as opt
from scipy.special import erf
from scipy.integrate import odeint
import matplotlib.pyplot as plt

__all__ = ["Pendulum"]


class Pendulum:
    
    def __init__(self,b=1,ell=1,g=9.8,m=1):
        """
        Initialize pendulum parameters
        
        ---------
        Parameters
        ---------
        b: float
            damping coefficient
        ell: float
            length of string
        g: float
            acceleration due to gravity
            default value is 9.8 m/s
        m: float
            bob mass
        """
        self.b = b
        self.ell = ell
        self.g = g
        self.m = m
        self.ys = None
        
    def eqns_of_motion(y,t,self):
        """
        Calculate the derivatives at a given time and set of theta values
        
        ----------
        Parameters
        ----------
        y : numpy array
            values of theta1 and theta2
        t : float
            time at which to evaluate
        
        -------
        Returns
        -------
        darray : numpy array
            the first derivatives at time t
        """
        
        th1 = y[0]
        th2 = y[1]
        dth1dt = th2
        dth2dt = -(self.b / self.m) * th2 - (self.g / self.ell) * np.sin(th1)
        return np.array([dth1dt,dth2dt])
        
    def simulate(self,y0,ts):
        """
        Call odeint to simulate the pendulum over time
        
        ----------
        Parameters
        ----------
        y0 : numpy array
            array of initial values for theta1 and theta2
        ts : numpy array
            time points for which to solve for y
        """
        self.ys = odeint(Pendulum.eqns_of_motion,y0,ts,args=(self,))
        

    def savedata(self,fname):
        """
        Save data as a csv file with one column for theta1 and one for theta2
        
        ----------
        Parameters
        ----------
        fname : string
            name of string to save file to
        """
        ydf = pd.DataFrame(data = self.ys, columns = ['theta1','theta2'])
        ydf.to_csv(ydf)
        
    def dummytest(self):
        return True
    
if __name__ == "__main__":
    NewPendulum = Pendulum()
    ts = np.linspace(0,20,100)
    NewPendulum.simulate(np.array([0,5]),ts)
    plt.figure()
    plt.plot(ts,NewPendulum.ys[:,0])
    plt.figure()
    plt.plot(NewPendulum.ys[:,0],NewPendulum.ys[:,1])
