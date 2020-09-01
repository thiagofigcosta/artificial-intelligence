#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sys,getopt

def plotLinearRegressionSingle(data,error,a,b,alpha,epoach):
    plt.xlabel('Iteration Number')
    plt.ylabel('Quadratic Error')
    plt.title('Error over Iteration')
    plt.plot(error)
    plt.figure().canvas.set_window_title('Size of Population X Profits of Food Trucks')

    plt.scatter(*zip(*data), marker="x", s=30)
    sizeOfPopulation, _ = zip(*data)
    plt.plot(sizeOfPopulation, [evaluateRegression(a,b,x)for x in sizeOfPopulation], label = 'y = {:.4f} + {:.4f}*x\nalpha = {:g}, epoach = {:d}'.format(b, a, alpha, epoach), color="green")
    plt.legend(loc='lower right')
    plt.xlabel('Size of Population')
    plt.ylabel('Profits of Food Trucks')
    plt.title('Size of Population X Profits of Food Trucks')
    fig = plt.figure(1)
    fig.canvas.set_window_title('Error over Iteration')
    plt.show()

def plotLinearRegressionMulti(A, b, error,alpha,epoach):
    plt.xlabel('Iteration Number')
    plt.ylabel('Quadratic Error')
    plt.title('Error over Iteration')
    s="y = "
    for i, a in enumerate(A):
        s+='{:.4f}'.format(a)+"*x"+str(i+1)+" + "
    s+='{:.4f}'.format(b)
    plt.plot(error, label = '{:s}\nalpha = {:g}, epoach = {:d}'.format(s,alpha, epoach))
    plt.legend(loc='lower right')
    plt.show()

def randomizeArray(array):
    np.random.shuffle(array)

def evaluateRegression(A, b, X):
    if isinstance(A, float):
        A=[A]
    if isinstance(X, float):
        X=[X]
    y=0
    for i in range(len(A)):
        y+=A[i]*X[i]
    return y+b


def readFromFile(path):
    fileData = open(path, 'r') 
    lines = fileData.readlines() 
    array=[]
    for line in lines: 
        array.append(list(float(el) for el in line.split(',')))
    return array

def calculateMean(data):
    mean=[0] * len(data[0])
    for house in data:
        for i in range(len(house)):
            mean[i]+=house[i]
    for i in range(len(mean)):
        mean[i]/=len(data)
    return mean

def calculateVariance(data):
    var=[0] * len(data[0])
    mean=calculateMean(data)
    for house in data:
        for i in range(len(house)):
            var[i]+=(house[i]-mean[i])**2
    for i in range(len(var)):
        var[i]/=(len(data)-1)
    return var

def calculateDeviation(data):
    var=calculateVariance(data)
    return [el**0.5 for el in var] 

def normalEquation(path):
    data=readFromFile(path)
    if path == "data2.txt":
        normalize(data)
    Xarr=[1]  
    Xarr.extend(data[0][:-1])
    X=np.array(Xarr)
    Y=np.array(data[0][-1:])
    for el in data[1:]:
        Xarr=[1]  
        Xarr.extend(el[:-1])
        X = np.vstack([X, Xarr])
        Y = np.vstack([Y, el[-1:]])
    Xt=X.transpose()
    XtXminus1=np.linalg.inv(Xt.dot(X))
    teta=XtXminus1.dot(Xt).dot(Y)

    A=list(*zip(*teta.tolist()))
    b=A[0]
    A=A[1:]
    print("A",A)
    print("b",b)
    quadraticError=0
    for el in data:
        expected = el[len(data[0])-1]
        evaluated = evaluateRegression(A,b,el[:-1])
        error=(evaluated-expected)
        quadraticError+=(error**2)
    quadraticError=0.5/len(data)*quadraticError
    print("quadraticError",quadraticError)

def normalize(data):
    mean=calculateMean(data)
    dev=calculateDeviation(data)
    print("Mean:",mean)
    print("Deviation:",dev)
    for el in data:
        for i in range(len(dev)):
            el[i]/=dev[i]

def singleVariables(alpha,epoach):
    data=readFromFile('data1.txt')
    A,b,qErrorArray= linearRegression(data,alpha,epoach)
    print("A",A)
    print("b",b)
    print("quadraticError",qErrorArray[-1])
    plotLinearRegressionSingle(data,qErrorArray,A[0],b,alpha,epoach)

def multipleVariables(alpha,epoach):
    data=readFromFile('data2.txt')
    normalize(data)
    A,b,qErrorArray= linearRegression(data,alpha,epoach)
    print("A",A)
    print("b",b)
    print("quadraticError",qErrorArray[-1])
    plotLinearRegressionMulti(A, b, qErrorArray, alpha,epoach)

def linearRegression(data,alpha,epoach):
    A = [1] * (len(data[0])-1)
    b = 1
    qErrorArray = []
    batchSize=len(data)
    for _ in range(epoach):
        randomizeArray(data)
        quadraticError=0
        errorArray = []
        for el in data:
            expected = el[len(data[0])-1]
            evaluated = evaluateRegression(A,b,el[:-1])
            error=(evaluated-expected)
            errorArray.append(error)
            quadraticError+=(error**2)
        qErrorArray.append(0.5/batchSize*quadraticError)
        # adjust parameters
        for i in range(len(A)):
            relativeError=0
            for j in range(len(data)):
                el=data[j]
                error=errorArray[j]
                relativeError+=error*el[i]
            A[i]=A[i]-(alpha/batchSize*relativeError)
        b=b-(alpha/batchSize*error)
    return A,b,qErrorArray



def main(argv):
    alpha = 0.01
    epoach = 2
    mode=""
    helpStr='linearRegression.py (--single | --multi | --normal1 | --normal2) [-a <value>] [-e <value>]'
    try:
        opts, args = getopt.getopt(argv,"ha:e:",["alpha=","epoachs=","single","multi","normal1","normal2"])
    except getopt.GetoptError:
        print (helpStr)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (helpStr)
            sys.exit()
        elif opt in ("-a", "--alpha"):
            alpha = float(arg)
        elif opt in ("-e", "--epoachs"):
            epoach = int(arg)
        elif opt in ("--single"):
            mode = "s"
        elif opt in ("--multi"):
            mode = "m"
        elif opt in ("--normal1"):
            mode = "n1"
        elif opt in ("--normal2"):
            mode = "n2"

    if mode=="":
        print (helpStr)
        sys.exit(2)
    elif mode=="s":
        singleVariables(alpha,epoach)
    elif mode=="m":
        multipleVariables(alpha,epoach)
    elif mode=="n1":
        normalEquation("data1.txt")
    elif mode=="n2":
        normalEquation("data2.txt")

if __name__ == "__main__":
    main(sys.argv[1:])