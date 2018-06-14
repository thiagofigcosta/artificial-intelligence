#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import genetic as gen

eggholderminfinder=gen.Genetic(lambda x:-(x[1]+47)*np.sin(np.sqrt(abs(x[1]+(x[0]/2)+47)))-x[0]*np.sin(np.sqrt(abs(x[0]-(x[1]+47)))),2,500,403,520,True,0,0.7,True,-1500)
eggholderminfinder.run()
eggholderminfinder.showNotables()
# eggholderminfinder.showFinalPop()
eggholderminfinder.plot()


# eggholderminfinder=gen.Genetic(lambda x:-(x[1]+47)*np.sin(np.sqrt(abs(x[1]+(x[0]/2)+47)))-x[0]*np.sin(np.sqrt(abs(x[0]-(x[1]+47)))),2,500,-600,600,True,0.1,0.7,True,-1500)
# eggholderminfinder.run()
# eggholderminfinder.showNotables()
# # eggholderminfinder.showFinalPop()
# eggholderminfinder.plot()