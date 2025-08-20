# packages
import numpy as np

# initial values
TOL = 10**(-3)
N = 100
h = 0.001

# get derivative
def derivative (f, x, h):
    fp = (f(x+h) - f(x))/h
    return fp

# newton's method
def newton_method(f, x_0, TOL):
    x = np.array([x_0])
    for t in np.arrange(0, N):
        fp = derivative(f, x[t], h) 
        fpp = derivative(fp, x[t], h)
        x_new = x[t] - fp/fpp
        x = np.append(x, x_new)
        if abs(x[t+1] - x[t]) < TOL:
            myans = x[-1]
            break
        if N == 100: # gives answer if doesn't reach tolerance
            myans = x[-1]
            break
    return myans
        
    