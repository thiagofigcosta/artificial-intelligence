#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

#OK #criar vetor de pares/obj tamanho X(preenchido aleatoriamente de acordo com um intervalo) 

#avaliar
#[LOOP - definir previamente numero de geracao]
#fazer x=5 clones para cada anticorpo
#mutacao, mutar inversamente proporcional a aptidao (usar taxa de mutacao exponencial ao invez dos 10% fixo)
#avaliar
#pegar o melhor de cada grupo (multimodal, para monomodal clonar mais vezes os melhores, e pegar os 90% melhores de todos e introduzir 10% aleatorio)

class Subject(object):
		def __init__(self,numberOfInputs,minvalue,maxvalue,isFloat):
			if(isFloat==False):
				self.inputs=rd.sample(range(minvalue, maxvalue), numberOfInputs)
			else:
				self.inputs=[rd.uniform(minvalue,maxvalue) for i in range(numberOfInputs)]
			self.output=0

class Imunologic(object):
	def __init__(self,function=lambda x: 0, numberOfInputs=2,populationSize=100,minvalue=-100,maxvalue=100,isFloat=True,multimodal=True):
		self.function=function
		self.minval=minvalue
		self.maxval=maxvalue
		self.multimodal=multimodal
		self.min=[]
		self.med=[]
		self.max=[]
		self.population = [ Subject(numberOfInputs,minvalue,maxvalue,isFloat) for i in range(populationSize) ]

	def evaluate(self):
		for i in range(len(self.population)):
			self.population[i].output=self.function(self.population[i].inputs)