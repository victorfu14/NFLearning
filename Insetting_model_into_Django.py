#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
import numpy as np
import pandas as pd
imported=tf.saved_model.load("/Users/sunao2000/Desktop") #this is code of how the model is imported
outputs = imported(tf.convert_to_tensor(testinp, dtype=tf.float32)) #This is the final output, the variable "testinp" is any numpy array with shape[x,11]
#The output with size[x,2] numpyarray type, such as [0.4323,0.547]. 
#If  left > right column, then the web should print "lost", and left < right column is "win". In the case of "[0.4323,0.547]", the final output is lost.
