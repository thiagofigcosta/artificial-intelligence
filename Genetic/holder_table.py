#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import genetic as gen


holdertable=lambda x:-np.abs(np.sin(x[0])*np.cos(x[1])*math.exp(np.abs(1-(np.sqrt(x[0]*x[0]+x[1]*x[1])/math.pi))))
holdertableminfinder=gen.Genetic(holdertable,2,100,-10,10,True,0.1,0.7,True,-200,True)
holdertableminfinder.run()
holdertableminfinder.showNotables()
#holdertableminfinder.showPopulation()
holdertableminfinder.plot()
 
