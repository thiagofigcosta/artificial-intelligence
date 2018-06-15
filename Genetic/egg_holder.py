#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import genetic as gen

eggholderminfinder=gen.Genetic(lambda x:-(x[1]+47)*np.sin(np.sqrt(abs(x[1]+(x[0]/2)+47)))-x[0]*np.sin(np.sqrt(abs(x[0]-(x[1]+47)))),2,300,-512,512,True,0.1,0.7,True,-1500,True)
eggholderminfinder.run()
eggholderminfinder.showNotables()
#eggholderminfinder.showFinalPop()
eggholderminfinder.plot()
