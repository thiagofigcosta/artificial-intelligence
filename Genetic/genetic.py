#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

class Subject(object):
		def __init__(self,numberOfInputs,minvalue,maxvalue,isFloat):
			if(isFloat==False):
				self.inputs=rd.sample(range(minvalue, maxvalue), numberOfInputs)
			else:
				self.inputs=[rd.uniform(minvalue,maxvalue) for i in range(numberOfInputs)]
			self.output=0
			self.fitness=0
			self.rouletteval=0
		def __lt__(self, other):
			return self.fitness<other.fitness

class Genetic(object):
	def __init__(self,function=lambda x: 0, numberOfInputs=2,populationSize=100,minvalue=-100,maxvalue=100,isFloat=True,mutationRate=0.1,fertilityRate=0.7,minimization=False,minOutputValue=0,relativeRank=True):
		if(populationSize%2!=0):
			populationSize=populationSize+1
		self.mutationRate=mutationRate
		self.fertilityRate=fertilityRate
		self.function=function
		self.offset=abs(minOutputValue)
		self.module=1
		self.minval=minvalue
		self.maxval=maxvalue
		self.relativeRank=relativeRank
		if(minimization==True):
			self.module=-1
		self.min=[]
		self.med=[]
		self.max=[]
		self.population = [ Subject(numberOfInputs,minvalue,maxvalue,isFloat) for i in range(populationSize) ]

	def evaluate(self):
		for i in range(len(self.population)):
			self.population[i].output=self.function(self.population[i].inputs)
			self.population[i].fitness=self.population[i].output*self.module+self.offset
		if(self.relativeRank==True):
			maxi=False
			if(self.module==1):
				maxi=True
			self.population.sort(reverse=maxi)
			a=self.population[0].fitness
			b=self.population[len(self.population)-1].fitness
			if(self.module==1):
				c=a
				a=b
				b=c
			for i in range(len(self.population)):
				print(self.population[i].fitness)
				self.population[i].fitness=a+(((b-a)*(i))/(len(self.population)-1))
				print(self.population[i].fitness)

	def mutate(self):
		def genrand():
			r=rd.uniform(0,1)
			n=0
			if(r<=0.6):
				n=rd.uniform(0,0.1)
			elif(r<=0.8):
				n=rd.uniform(0.09,0.16)
			elif(r<=0.95):
				n=rd.uniform(0.15,0.23)
			else:
				n=rd.uniform(0,0.666)
			n=1+n
			if(rd.choice([True, False])):
				n=-n
			return n

		for i in range(len(self.population)):
			for j in range(len(self.population[i].inputs)):
				if(rd.uniform(0,1)<self.mutationRate):
					self.population[i].inputs[j]=self.population[i].inputs[j]*genrand()
					if(self.population[i].inputs[j]<self.minval):
						self.population[i].inputs[j]=self.minval
					if(self.population[i].inputs[j]>self.maxval):
						self.population[i].inputs[j]=self.maxval

	def sex(self,father,mother):
		if(rd.uniform(0,1)<self.fertilityRate):
			for i in range(len(father.inputs)):
				randnumber=rd.uniform(0,1)
				child0=randnumber*father.inputs[i]+(1-randnumber)*mother.inputs[i]
				child1=(1-randnumber)*father.inputs[i]+randnumber*mother.inputs[i]
				father.inputs[i]=child0
				mother.inputs[i]=child1
		return father.inputs,mother.inputs

	def initroulette(self):
		self.population[0].rouletteval=self.population[0].fitness
		for i in range(len(self.population)-1):
			self.population[i+1].rouletteval=self.population[i].rouletteval+self.population[i+1].fitness
			if(self.population[i+1].rouletteval<self.population[i].rouletteval):
				self.offset=self.offset*1.1+1000
				self.evaluate()	
				self.initroulette()	

	def getroulletsubject(self):	
		if(self.relativeRank==True):	
			sortednumber=rd.uniform(0,self.population[len(self.population)-1].rouletteval) 
		else:
			sortednumber=rd.uniform(self.offset,self.population[len(self.population)-1].rouletteval) 
		for i in range(len(self.population)):
			if(sortednumber<=self.population[i].rouletteval):
				print ('GOTTTT: ',i),
				return copy.deepcopy(self.population[i])

	def nxtgen(self):
		# for i in range(len(self.population)):
		# 	print (i,': ',self.population[i].output,'-',self.population[i].fitness,'___',self.population[i].rouletteval)
		# print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')

		self.initroulette()


		for i in range(len(self.population)):
			print (i,': ','x:',self.population[i].inputs[0],'y:',self.population[i].inputs[1],'output: ',self.population[i].output,' fitness:',self.population[i].fitness,' roleta:',self.population[i].rouletteval)
		print ('.    ..    ..    ..    ..    ..    ..    ..    ..    .')
		
		newpopulation=copy.deepcopy(self.population)
		for i in range(len(self.population)//2):
			newpopulation[i*2].inputs,newpopulation[i*2+1].inputs=self.sex(self.getroulletsubject(),self.getroulletsubject())
			print()
		self.population=newpopulation
		self.evaluate()
		for i in range(len(self.population)):
			print (i,': ','x:',self.population[i].inputs[0],'y:',self.population[i].inputs[1],'output: ',self.population[i].output,' fitness:',self.population[i].fitness,' roleta:',self.population[i].rouletteval)
		print ('------------------------------------------------------')

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

	def plot(self):
		plt.plot(self.min)
		plt.plot(self.med)
		plt.plot(self.max)
		plt.legend(['min', 'med', 'max'], loc='upper left')
		plt.show()

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
		print('Minimum Subject x*=y', inI,'=',i)
		print('Maximum Subject x*=y', inA,'=',a)

	def showFinalPop(self):
		print ('Populacao final (x* = y):')
		for i in range(len(self.population)):
			print(self.population[i].inputs,'=',self.population[i].output)

	def run(self,maxgens=100):
		self.min=[]
		self.med=[]
		self.max=[]
		self.evaluate()
		for i in range(maxgens):
			self.nxtgen()
			#self.mutate()
			self.evaluate()
			self.rank()

