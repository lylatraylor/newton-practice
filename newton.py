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
def newton_method(f, x_0, TOL = 1e-4):
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
    x_new = x0 - derivative(f, x0)/ derivative_2(f, x0)
    x = x0
    while abs(x_new - x) > TOL:
        x = x_new
        x_new = x0 - derivative(f, x0)/ derivative_2(f, x0)

    return {"x": x_new,
            'value': f(x_new)}

        
    