# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 23:34:33 2018

Roll No: 18AT91R02
Name: Arvind Kumar Gupta
Assignment No.: 4

"""

#%%
import pandas as pd
import math
import operator
import numpy as np
#%%
train_set = pd.read_csv('data4.csv', header=None)
train_set = train_set.values
test_set = pd.read_csv('test4.csv', header=None)
test_set = test_set.values

#%% Distance Measure
def euclideanDist(data1, data2, length):
    dist = 0
    for i in range (length):
        dist += pow((data1[i] - data2[i]), 2)
    return math.sqrt(dist)    

#%%
 
def getNeighbors(trainSet, testData, k):
    distances = []
    length = len(testData)-1
    for i in range(len(trainSet)):
        dist = euclideanDist(testData, trainSet[i], length)
        distances.append((trainSet[i], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

#%%
def getResponse(neighbors):
    classVotes = {}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


#%%
    
def main():
    predictions=[]
    k=5
    for i in range(len(test_set)):
        neighbors = getNeighbors(train_set, test_set[i], k)
        result = getResponse(neighbors)
        predictions.append(result)
    
    return np.array(predictions, dtype = int)

#%%
classf= main()
np.set_printoptions(threshold=np.nan)
print (classf)

f2= open("18AT91R02_4.out","w+")
f2.write(str(classf))
f2.close()
