#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
import numpy as np
import pandas as pd

inputdata=xxxxxxx #the numpyarray with size[x,11]
imported=tf.saved_model.load("/Users/sunao2000/Desktop") #this is code of how the model is imported, please change this directory into correct one.
outputs = imported(tf.convert_to_tensor(inputdata, dtype=tf.float32))#This is the final output, the variable "inputdata" is any numpy array with shape[x,11]
output=outputs.numpy()
#The output with size[x,2] numpyarray type, such as [0.4323,0.547]. 
final_output=[]
output=outputs.numpy()
for i in range(output.shape[0]):
    if(output[i,0]>output[i,1]):
        final.append(0)
    if(output[i,0]<output[i,1]):
        final.append(1)
#final_output is the final result with list type[x,1],for each row,0 means lost, and 1 means win.