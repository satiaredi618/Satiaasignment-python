import numpy as np
from scipy.integrate import dblquad

# Function to integrate
def integrand(y, x):
    return x**2 + y**2

# Limits for x and y
volume, error = dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1)
print("Volume under the surface:", volume)
