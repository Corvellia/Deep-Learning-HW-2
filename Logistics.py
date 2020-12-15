import random
from sigmoid import *

def Logistics(E, eta, iterations):
    w = []
    w.append(random.randint(-50, 50))
    w.append(random.randint(-50, 50))
    w.append(random.randint(-50, 50))

    for z in range(int(iterations)):
        for k in range(0, len(E)):
            x0 = 1.0
            x1 = float(E[k][0])
            x2 = float(E[k][1])
            ye = float(E[k][2])

            #print("X1: " + str(x1))
            #print("X2: " + str(x2))
            #print ("Y: " + str(ye))
            yCap = float(w[0] * x0) + float(w[1] * x1) + float(w[2] * x2)
            #print("Pre Sigma: " + str(yCap))
            yCap = sigmoid(yCap)
            #print("Ycap: " + str(yCap))
            delta = float(ye - yCap) #float((ye - yCap) * yCap * (1-yCap))
            update = float(eta * delta * yCap * (1 - yCap))

            #print("Delta: " + str(delta))
            w[0] = float(w[0] + update * x0)
            w[1] = float(w[1] + update * x1)
            w[2] = float(w[2] + update * x2)
            

    return w