import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import Normalize
#SYNTHETIC DATA
np.random.seed(0)
X = np.random.rand(100, 1)#100 SAMPLES, 1 FEATURE
y = 3 * X.squeeze() + 2 + np.random.randn(100)#LINEAR RELATION WITH NOISE
#Functions
def compute_gradient(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    errors = predictions - y
    gradient = (1/m) * X.T.dot(errors)
    return gradient
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    errors = predictions - y
    cost = (1/(2*m)) * np.sum(error**2)
    return cost
    