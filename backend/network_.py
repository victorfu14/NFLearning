#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


def multilayer_perceptron(x, weights, biases):
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    out_layer = tf.matmul(layer_1, weights['out']) + biases['out']
    return out_layer

def n_n(x,w1,w2,w3,b1,b2,b3):
    x1=multilayer_perceptron(x, w1, b1)
    x2=multilayer_perceptron(x1,w2,b2)
    x3=multilayer_perceptron(x2,w3,b3)
    return x3

def train(x,y):
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=x, labels=y))
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(cost)


# In[ ]:




