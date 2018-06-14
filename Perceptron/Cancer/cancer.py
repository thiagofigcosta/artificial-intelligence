#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import perceptron as pn

#Carrega o arquivo
data=pd.read_csv('breast-cancer-wisconsin.data',names=['ID','Clump Thickness',' Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class'])
#Trata duvidas como 0
for i, row in data.iterrows():
    t=row['Bare Nuclei']
    if(t=='?'):
        data.loc[i,'Bare Nuclei'] = 0
#Separa um tipo de neuronio para cada tipo de cancer
for i, row in data.iterrows():
    t=row['Class']
    if(t==2):
        data.loc[i,'y1'] = 1.0
        data.loc[i,'y2'] = 0.0
    if(t==4):
        data.loc[i,'y1'] = 0.0
        data.loc[i,'y2'] = 1.0
data=data.drop(['ID'],axis=1)
data=data.drop(['Class'],axis=1)
#Converte os campos para inteiro
data=data.apply(lambda x: pd.to_numeric(x,downcast='integer'))
#randomiza a amostra
data=data.sample(frac=1)#random_state=number fixa o aleatorio fazendo com que sempre selecione os mesmos indices
#Seleciona 66% da amostra para treino
train=data.sample(frac=0.66) 
#pega o restante da amostra para teste
test=data.drop(train.index)
#separa entradas e saidas de treino e teste
X_train=train.drop(['y1','y2'],axis=1)
D_train=train.drop(X_train.columns.tolist(),axis=1)
X_test=test.drop(['y1','y2'],axis=1)
D_test=test.drop(X_test.columns.tolist(),axis=1)
#converte em matrizes
X_train=np.matrix(X_train.values)
D_train=np.matrix(D_train.values)
X_test=np.matrix(X_test.values)
D_test=np.matrix(D_test.values)
#treina
p=pn.Perceptron()
W,b,Err=p.train(1000,0.1,X_train,D_train)
#testa
acc,out=p.evaluate(W,b,X_test,D_test)
print('Accuracy =', acc)
