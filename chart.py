import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import base64
from io import BytesIO

def getGraphFig(symbol, history):

    fig = Figure()
    ax = fig.subplots()
    
    ypoints = []
    xpoints = []


    for i in range(len(history["Close"])):
        ypoints.append(history["Close"][i])
        xpoints.append(i)

    ax.plot(xpoints, ypoints)
    
    return fig
    



    #make line going down red, and line going up green
    #make axis lables according to interval
    plt.title("Daily close value of " + str(symbol))
    plt.ylabel("Closing price")
    plt.plot(ypoints)
    plt.show()