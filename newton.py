# packages
import numpy as np

# initial values
TOL = 10**(-3)
N = 100
h = 0.001

# get derivatives
def derivative (f, x, h):
    return (f(x+h) - f(x))/h

def derivative_2 (f, x, h):
    return (f(x+2*h) - 2*f(x+h) + f(x))/ h*h

# newton's method
def newton_method(f, x_0, TOL):
    """ Run Newton's method to minimize a function.

    Parameters
    ----------
    x0: starting value
    f: function
    TOL: tolerance
    
    Returns
    -------
    value of x that minimizes the function.
    
    """
    x = np.array([x_0])
    for t in np.arrange(0, N):
        fp = derivative(f, x[t], h) 
        fpp = derivative_2(f, x[t], h)
        x_new = x[t] - fp/fpp
        x = np.append(x, x_new)
        if abs(x[t+1] - x[t]) < TOL:
            myans = x[-1]
            break
        if N == 100: # gives answer if doesn't reach tolerance
            myans = x[-1]
            break
    return myans
        
    