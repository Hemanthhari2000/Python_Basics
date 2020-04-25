import matplotlib.pyplot as plt
import numpy as np
x=[21,22,23,4,5,6,7,1,8,9,10,31,32,33,36,37,50,55,60]
num_bins=6
n,bins,patches=plt.hist(x,num_bins,facecolor="blue")
plt.show()
 
