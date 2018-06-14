#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import perceptron as pn

#Carrega o arquivo
data=pd.read_csv('wine.data',names=['Tipo','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline'])
#Converte os campos para float
data=data.apply(lambda x: pd.to_numeric(x,downcast='float'))
#Separa um tipo de neuronio para cada tipo de vinho
data['y1']=0
data['y2']=0
data['y3']=0
for i, row in data.iterrows():
    t=row['Tipo']
    if(t==1):
        data.loc[i,'y1'] = 1.0
        data.loc[i,'y2'] = 0.0
        data.loc[i,'y3'] = 0.0
    if(t==2):
        data.loc[i,'y1'] = 0.0
        data.loc[i,'y2'] = 1.0
        data.loc[i,'y3'] = 0.0
    if(t==3):
        data.loc[i,'y1'] = 0.0
        data.loc[i,'y2'] = 0.0
        data.loc[i,'y3'] = 1.0
data=data.drop(['Tipo'],axis=1)
#randomiza a amostra
data=data.sample(frac=1)#random_state=number fixa o aleatorio fazendo com que sempre selecione os mesmos indices
#Seleciona 66% da amostra para treino
train=data.sample(frac=0.66) 
#pega o restante da amostra para teste
test=data.drop(train.index)
#separa entradas e saidas de treino e teste
X_train=train.drop(['y1','y2','y3'],axis=1)
D_train=train.drop(X_train.columns.tolist(),axis=1)
X_test=test.drop(['y1','y2','y3'],axis=1)
D_test=test.drop(X_test.columns.tolist(),axis=1)
#converte em matrizes
X_train=np.matrix(X_train.values)
D_train=np.matrix(D_train.values)
X_test=np.matrix(X_test.values)
D_test=np.matrix(D_test.values)
#treina
p=pn.Perceptron()
W,b,Err=p.train(1000,0.02,X_train,D_train)
#testa
acc,out=p.evaluate(W,b,X_test,D_test)
print('Accuracy =', acc)
