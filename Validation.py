from sigmoid import *

def validation(V, w):
    result = 0
    for k in range(0, len(V)):
        x0 = 1
        x1 = V[k][0]
        x2 = V[k][1]
        ye = float(V[k][2])

        yCap = float(w[0] * x0) + float(w[1] * x1) + float(w[2] * x2)
        yCap = sigmoid(yCap)
        tempResult = float(ye - yCap)
        tempResult = float(tempResult * tempResult)
        result += tempResult

    return result