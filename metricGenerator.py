import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
import math
from matplotlib.widgets import Slider, Button, RadioButtons
#takes the p-norm of a given vector, for infinity norm write p = inf
def l_p_metric(vec, p = 2):
    dist = 0
    point = list(map(lambda x: abs(x), vec))
    if p == "inf":
        return max(point)
    for i in range(len(point)):
        dist += math.pow(point[i],p)
    dist = math.pow(dist, 1/p)
    return dist

def discrete_metric(vec):
    if len(np.unique(vec) != len(vec)):
        return 1
    return 0

def helly_metric():
    pass

def hamming_metric():
    pass

def euclid_dist(p1, p2):
    dist = math.pow(math.pow(p1[0] - p2[0],2) + math.pow(p1[1] - p2[1],2), 0.5)
    return dist

def unitBall(distri = "gaussian", connected = True, p = 2):
    points = np.random.normal(size=(2,100))
    if distri != "gaussian":
        pass
    for i in range(len(points[0])):
        norm = l_p_metric((points[0][i],points[1][i]), "inf")
        points[0][i] = points[0][i] / norm
        points[1][i] = points[1][i] / norm

    #fig, ax = plt.subplots()


    fig,ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)
    N = 300
    theta = list( map( lambda x: x*2*math.pi / N, list(range(0,N)) ) )
    graph_points = list( map(lambda x: ( math.cos(x), math.sin(x) ), theta) )
    graph_points = list( map(lambda x: ( x[0]/l_p_metric(x,p), x[1]/l_p_metric(x,p) ), graph_points ) )
    graph_points.append(graph_points[0])

    l, = plt.plot(*zip(*graph_points))
    plt.title('Unit Ball with P-Norm')
    plt.axis('scaled')
    plt.grid()
    axPval = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor = 'lightgoldenrodyellow')
    pVal = Slider(axPval, 'P-Norm:', 0.1, 10.0, valinit = p)

    if connected == False:
        l, = plt.scatter(*zip(*graph_points))

    def update(val):
        theta = list( map( lambda x: x*2*math.pi / N, list(range(0,N)) ) )
        graph_points = list( map(lambda x: ( math.cos(x), math.sin(x) ), theta) )
        graph_points = list( map(lambda x: ( x[0]/l_p_metric(x,pVal.val), x[1]/l_p_metric(x,pVal.val) ), graph_points ) )
        graph_points.append(graph_points[0])
        l.set_data(*zip(*graph_points))

    pVal.on_changed(update)
    plt.show()

unitBall()
