#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import imunologic as imu

easom=lambda x:-(-np.cos(x[0])*np.cos(x[1])*math.exp(-(math.pow(x[0]-math.pi,2)+math.pow(x[1]-math.pi,2))))

print('MULTIMODAL')
easomminfinder=imu.Imunologic(easom,2,500,-10,10,True,4,100,False,-1500,True)
easomminfinder.run(10)
easomminfinder.showNotables()
#easomminfinder.showPopulation()
easomminfinder.plot()

print('\nMONOMODAL')
easomminfinder=imu.Imunologic(easom,2,500,-10,10,True,4,100,False,-1500,False)
easomminfinder.run(100)
easomminfinder.showNotables()
#easomminfinder.showPopulation()
easomminfinder.plot()