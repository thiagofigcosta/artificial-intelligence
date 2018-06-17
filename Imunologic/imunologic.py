#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import math
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

class Imunologic(object):
	class Subject(object):
		def __init__(self,numberOfInputs,minvalue,maxvalue,isFloat):
			if(isFloat==False):
				self.inputs=rd.sample(range(minvalue, maxvalue), numberOfInputs)
			else:
				self.inputs=[rd.uniform(minvalue,maxvalue) for i in range(numberOfInputs)]
			self.output=0
			self.fitness=0
		def __lt__(self, other):
			return self.output<other.output

	def __init__(self,function=lambda x: 0, numberOfInputs=2,populationSize=100,minvalue=-100,maxvalue=100,isFloat=True,mmclones=5,smclones=50,minimization=True,minOutputValue=0,multimodal=True):
		self.function=function
		self.minval=minvalue
		self.maxval=maxvalue
		self.offset=abs(minOutputValue)
		self.mmclones=mmclones
		self.smclones=smclones
		self.minimization=minimization
		self.module=1
		if(minimization==True):
			self.module=-1
		self.multimodal=multimodal
		self.initialsize=populationSize
		self.numberOfInputs=numberOfInputs
		self.isFloat=isFloat
		self.min=[]
		self.med=[]
		self.max=[]
		self.population = [ self.Subject(numberOfInputs,minvalue,maxvalue,isFloat) for i in range(populationSize) ]

	def evaluate(self):
		for i in range(len(self.population)):
			self.population[i].output=self.function(self.population[i].inputs)
			self.population[i].fitness=self.population[i].output*self.module+self.offset
		if(self.multimodal==False):
			self.population.sort(reverse=not self.minimization)

	def clone(self):
		for i in range(len(self.population)):
			if(self.multimodal==True):
				for j in range(self.mmclones):
					self.population.insert(i*self.mmclones+1+i,copy.deepcopy(self.population[i*self.mmclones+i]))
			else:
				for j in range(int(self.smclones/(i+1))):
					self.population.append(copy.deepcopy(self.population[i]))

	def rangesort(self,lst,start,end,rev=False):
		lst=lst[0:start]+sorted(lst[start:end+1],reverse=rev)+lst[end+1:len(lst)]
		return lst

	def mutate(self):
		def genrand():
			r=rd.uniform(0,1)
			n=0
			if(r<=0.3):
				n=rd.uniform(0,0.06)
			elif(r<=0.8):
				n=rd.uniform(0,0.11)
			elif(r<=0.9):
				n=rd.uniform(0.09,0.16)
			elif(r<=0.97):
				n=rd.uniform(0.15,0.23)
			else:
				n=rd.uniform(0.333,0.666)
			n=1+n
			if(rd.choice([True, False])):
				n=-n
			return n
		maxx=-float("inf")
		for it in range(len(self.population)):
			if(self.population[it].fitness>maxx):
				maxx=self.population[it].fitness
		for i in range(len(self.population)):
			for j in range(len(self.population[i].inputs)):
				if(rd.uniform(0,1)<(math.exp(-(self.population[i].fitness/maxx)))):
					self.population[i].inputs[j]=self.population[i].inputs[j]*genrand()
					if(self.population[i].inputs[j]<self.minval):
						self.population[i].inputs[j]=self.minval
					if(self.population[i].inputs[j]>self.maxval):
						self.population[i].inputs[j]=self.maxval

	def select(self):
		if(self.multimodal==True):
			for i in range(0,len(self.population),self.mmclones):
				self.population=self.rangesort(self.population,i,(i+self.mmclones-1),(not self.minimization))
			for i in range(self.initialsize):
				self.population[i]=self.population[i*self.mmclones]
			self.population=self.population[0:self.initialsize]
		else:
			self.population.sort(reverse=not self.minimization)
			self.population=self.population[0:int(self.initialsize*0.9)]+[ self.Subject(self.numberOfInputs,self.minval,self.maxval,self.isFloat) for i in range(int(self.initialsize*0.1)) ]


	def rank(self):
		i=float("inf")
		e=0
		a=-float("inf")
		for it in range(len(self.population)):
			e=e+self.population[it].output
			if(self.population[it].output<i):
				i=self.population[it].output
			if(self.population[it].output>a):
				a=self.population[it].output
		e=e/len(self.population)
		self.min.append(i)
		self.med.append(e)
		self.max.append(a)

	def showNotables(self):
		i=float("inf")
		inI=[0,0]
		a=-float("inf")
		inA=[0,0]
		for it in range(len(self.population)):
			if(self.population[it].output<i):
				i=self.population[it].output
				inI=self.population[it].inputs
			if(self.population[it].output>a):
				a=self.population[it].output
				inA=self.population[it].inputs
		if(self.module==-1):
			print('Best Subject x*=y', inI,'=',i)
			print('Worst Subject x*=y', inA,'=',a)
		else:
			print('Best Subject x*=y', inA,'=',a)
			print('Worst Subject x*=y', inI,'=',i)
			

	def showPopulation(self):
		print ('Populacao (x* = y):')
		for i in range(len(self.population)):
			print(i,':',self.population[i].inputs,'=',self.population[i].output)

	def plot(self):
		plt.plot(self.min)
		plt.plot(self.med)
		plt.plot(self.max)
		if(self.module==-1):
			plt.legend(['Best', 'Avg.', 'Worst'], loc='upper left')
		else:
			plt.legend(['Worst', 'Avg.', 'Best'], loc='upper left')
		plt.show()

	def run(self,maxgens=100):
		self.min=[]
		self.med=[]
		self.max=[]
		self.evaluate()
		for i in range(maxgens):
			self.clone()
			self.mutate()
			self.evaluate()
			self.select()
			self.rank()
