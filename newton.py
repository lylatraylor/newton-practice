# packages
import numpy as np

# get derivatives
def derivative (f, x, h = 1e-8):
    return (f(x+h) - f(x)) / h

def derivative_2 (f, x, h = 1e-5):
    return (derivative(f, x+h, h) - derivative(f, x, h)) / h

# newton's method
def newton_method(f, x0, TOL = 1e-4):
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
        if derivative_2(f, x) == 0:
            break
        x_new = x - derivative(f, x)/ derivative_2(f, x)

    return {"x": x_new,
            'value': f(x_new)}

        
    