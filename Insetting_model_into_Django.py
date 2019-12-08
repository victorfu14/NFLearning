#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
import numpy as np
import pandas as pd
imported=tf.saved_model.load("/Users/sunao2000/Desktop") #this is code of how the model is imported
outputs = imported(tf.convert_to_tensor(testinp, dtype=tf.float32)) #the final output, the variable "testinp" is any numpy array with shape[x,11]

