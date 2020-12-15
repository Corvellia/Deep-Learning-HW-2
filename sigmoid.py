from  math import exp
import numpy

def sigmoid(x):
    numpy.seterr(over="ignore")
    #bottom = float(1 + numpy.exp(-x))
    #print("bottom: " + str(bottom))
    #print(float(1/bottom))
    #return (float(1/bottom))
    if x >= 0:
        #z = float(exp(-x))
        z = float(numpy.exp(-x))
        #print(z) 
        return float(1 / (1 + z))
    else:
        #z = float(exp(x))
        z = float(numpy.exp(x))
        #print(z)
        return float(z / (1 + z))