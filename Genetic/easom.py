#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import genetic as gen


easom=lambda x:-np.cos(x[0])*np.cos(x[1])*math.exp(-(math.pow(x[0]-math.pi,2)+math.pow(x[1]-math.pi,2)))
easomminfinder=gen.Genetic(easom,2,100,-100,100,True,0.1,0.7,True,-200,True)
easomminfinder.run()
easomminfinder.showNotables()
#easomminfinder.showPopulation()
easomminfinder.plot()
 
