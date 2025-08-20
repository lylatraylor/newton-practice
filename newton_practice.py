import numpy as np

TOL = 10**(-3)
N = 100

def first_derivative (f, x, h):
    fp = (f(x+h) - f(x))/h
    return fp

def newton_method(f, x0):
    x = np.array([x0])
    fp = diff(f, x)
    fpp = diff(fp, x)
    for t in ([0, N]):
        x[t+1] = x[t] - (fp[t]/fpp[t])
        x = np.append(x, x[t+1])
        if abs(x[t+1] - x[t]) < TOL:
            
        
        
    