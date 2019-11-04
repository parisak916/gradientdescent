import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import array as arr
import math

def gd_hw3(x1,x2,alpha,iter):

    iterations = iter

    x1 = 0
    x2 = 0 
    plt.figure()
#original equation:  f(x) = 3x1^2 + 2x2^2 + 4x1x2 – 5x1 + 6.
    for j in range(len(alpha)):
        for i in range(iterations):
            x1 = x1 - alpha[j]*(6*x1 + 4*x2)
            x2 = x2 - alpha[j]*(4*x2 + 4*x1 -5) 
            plt.scatter(x1,x2)
            
        plt.show()
        

#original equation: f(x) = sin(x) + 0.3x
def gd_h3_2(x, alpha, iter):
    plt.figure()
    plt.ylim((-10,10))
    for j in range(len(alpha)):
        for i in range(iter):
            x = x - alpha[j]*(math.cos(x)+.3)
            y = math.cos(x) +.3
            plt.scatter(x,y)
 
            
        plt.show()
        

#step function
alpha = arr.array('d',[.0001, .001, .01, .1, 1, 10])
x=2
# x starts at 2, different values of x converge at different local minimums
xfinal = gd_h3_2(x,alpha, iter=1000)
#gradient of x1 and x2 start at (0,0)
xfinal2 = gd_hw3(0,0,alpha, iter=1000)

