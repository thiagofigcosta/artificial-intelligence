#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import imunologic as imu


eggholder=lambda x:-(x[1]+47)*np.sin(np.sqrt(abs(x[1]+(x[0]/2)+47)))-x[0]*np.sin(np.sqrt(abs(x[0]-(x[1]+47))))

print('MULTIMODAL')
eggholderminfinder=imu.Imunologic(eggholder,2,500,-512,512,True,4,100,True,-1500,True)
eggholderminfinder.run(10)
eggholderminfinder.showNotables()
#eggholderminfinder.showPopulation()
eggholderminfinder.plot()

print('\nMONOMODAL')
eggholderminfinder=imu.Imunologic(eggholder,2,500,-512,512,True,4,100,True,-1500,False)
eggholderminfinder.run(100)
eggholderminfinder.showNotables()
#eggholderminfinder.showPopulation()
eggholderminfinder.plot()
