# packages
#Hi Lyla!!
import numpy as np
from scipy.differentiate import hessian
from scipy.differentiate import derivative

# get derivatives
def deriv (f, x, h = 1e-8):
    return (f(x+h) - f(x)) / h

def deriv_2 (f, x, h = 1e-5):
    return (deriv(f, x+h, h) - deriv(f, x, h)) / h

# newton's method
def optimize(x0, f, TOL = 1e-4):
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
    # conditioning
    if not np.isscalar(x0):
        raise TypeError('x0 must be numeric')
    if not callable(f):
        raise TypeError('f must be callable')
    
    x_new = x0 - deriv(f, x0)/ deriv_2(f, x0)
    x = x0
    while abs(x_new - x) > TOL:
        x = x_new
        if deriv_2(f, x) == 0:
            raise ZeroDivisionError("Second derivative is zero- Newton's method fails")
        x_new = x - deriv(f, x)/ deriv_2(f, x)

    return {"x": x_new,
            'value': f(x_new)}


# multivariate case
def multivariate():
    h_matrix = hessian(x0, f)
    gradient = derivative(f)
    x_new = [x0] -

        
    