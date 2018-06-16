#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np
import genetic as gen


shafter4=lambda x:0.5+(math.pow(np.cos(np.sin(np.abs(x[0]*x[0]+x[1]*x[1]))),2)-0.5)/math.pow((1+0.001*(x[0]*x[0]+x[1]*x[1])),2)
shafter4minfinder=gen.Genetic(shafter4,2,100,-100,100,True,0.1,0.7,True,-200,True)
shafter4minfinder.run()
shafter4minfinder.showNotables()
#shafter4minfinder.showPopulation()
shafter4minfinder.plot()
