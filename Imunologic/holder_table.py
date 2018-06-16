#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import imunologic as imu

holdertable=lambda x:-np.abs(np.sin(x[0])*np.cos(x[1])*math.exp(np.abs(1-(np.sqrt(x[0]*x[0]+x[1]*x[1])/math.pi))))

print('MULTIMODAL')
holdertableminfinder=imu.Imunologic(holdertable,2,500,-10,10,True,4,100,True,-1500,True)
holdertableminfinder.run(10)
holdertableminfinder.showNotables()
#holdertableminfinder.showPopulation()
holdertableminfinder.plot()

print('\nMONOMODAL')
holdertableminfinder=imu.Imunologic(holdertable,2,500,-10,10,True,4,100,True,-1500,False)
holdertableminfinder.run(100)
holdertableminfinder.showNotables()
#holdertableminfinder.showPopulation()
holdertableminfinder.plot()